import sys
from dataclasses import dataclass
from pprint import pformat
from typing import Iterable, List, Literal

import requests

from dataset import DATASET, DatasetItem

ES_URL = "http://localhost:9200"


@dataclass
class ValidationResult:
    status: Literal["ok", "error"]
    reason: str = ""
    es_hits: List[dict] = None
    es_response: dict = None


def eprint(text):
    print("\033[91m" + text + "\033[0m", file=sys.stderr)


def dprint(text):
    print("\033[90m" + text + "\033[0m")


def esdebug(resp):
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        eprint(pformat(resp.json()["error"]))
        raise


def index_name(item_id: int):
    return f"test_{item_id}"


def delete_index(item_id: int):
    resp = requests.delete(f"{ES_URL}/{index_name(item_id)}")
    if resp.status_code == 404:
        return
    esdebug(resp)


def create_index(item_id: int, item: DatasetItem):
    resp = requests.put(
        f"{ES_URL}/{index_name(item_id)}",
        json={
            "settings": {"number_of_shards": 1, "number_of_replicas": 1},
            "mappings": item.mappings,
        },
    )
    esdebug(resp)


def index_item(item_id: int, item: DatasetItem):
    for i, doc in enumerate(item.includes):
        doc_id = f"include_{i}"
        resp = requests.put(f"{ES_URL}/{index_name(item_id)}/_doc/{doc_id}", json=doc)
        esdebug(resp)

    for i, doc in enumerate(item.excludes):
        doc_id = f"exclude_{i}"
        resp = requests.put(f"{ES_URL}/{index_name(item_id)}/_doc/{doc_id}", json=doc)
        esdebug(resp)


def wait_for_index(item_id: int):
    resp = requests.get(f"{ES_URL}/{index_name(item_id)}/_refresh")
    esdebug(resp)


def verify_query(item_id: int, item: DatasetItem, query: dict) -> ValidationResult:
    resp = requests.post(
        f"{ES_URL}/{index_name(item_id)}/_search", json={"query": query}
    )
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        return ValidationResult(
            status="error",
            reason=f"Failed to execute query: {e}",
            es_response=resp.json(),
        )

    hits = resp.json()["hits"]["hits"]

    try:
        assert len(hits) == len(item.includes)
        assert all(hit["_id"].startswith("include_") for hit in hits)
    except AssertionError as e:
        return ValidationResult(
            status="error",
            reason="Invalid documents returned.",
            es_hits=hits,
        )

    return ValidationResult(status="ok")


def validate(item_id: int, item: DatasetItem, query: dict) -> ValidationResult:
    delete_index(item_id)
    try:
        create_index(item_id, item)
        index_item(item_id, item)
    except requests.HTTPError as e:
        return ValidationResult(
            status="error",
            reason="Failed to setup index",
            es_response=e.response.json(),
        )
    wait_for_index(item_id)
    return verify_query(item_id, item, query)


def validate_all(items: Iterable[DatasetItem]):
    for item_id, item in enumerate(items):
        r = validate(item_id, item, item.query)
        if r.status == "ok":
            dprint(f"Item {item_id}: OK")
        else:
            eprint(f"Item {item_id}: {pformat(r)}")


if __name__ == "__main__":
    validate_all(DATASET)
