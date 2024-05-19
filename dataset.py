from dataclasses import dataclass
from typing import *


@dataclass
class DatasetItem:
    text: str  # Input text.
    clarification: str  # Clarification for the model, training only.
    includes: List[dict]  # Matching documents.
    excludes: List[dict]  # Non-matching documents.
    mappings: dict  # ElasticSearch `mappings` index definition.
    query: dict  # Expected ElasticSearch query.



DATASET: List[DatasetItem] = [
    DatasetItem(
        text="john smith",
        clarification='Phrase "john smith" is a common name, we should query "full_name" field.',
        includes=[{"full_name": "john smith", "age": 25}],
        excludes=[{"full_name": "adam doe", "age": 30}],
        mappings={"properties": {"full_name": {"type": "text"}}},
        query={"match": {"full_name": "john smith"}},
    ),
    DatasetItem(
        text="older than 30",
        clarification="We should query the 'age' field.",
        includes=[{"full_name": "john smith", "age": 35}],
        excludes=[{"full_name": "adam doe", "age": 27}],
        mappings={"properties": {"age": {"type": "integer"}}},
        query={"range": {"age": {"gt": 30}}},
    ),
]
