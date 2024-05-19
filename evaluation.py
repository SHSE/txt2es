import json
import random
from dataset import DatasetItem
from llms import ask_gpt
from synthetic import SYHTHETIC_DATASET
from validation import validate

QUERY_PROMPT = """
You are an AI designed to convert a text to an ElasticSearch query.

Here is the ElasticSearch index to query:
```json
{index_definition}
```

Here is the input text:
```
{text}
```

Output the query in JSON format.
"""


def query_prompt(item: DatasetItem) -> str:
    return QUERY_PROMPT.format(
        index_definition=json.dumps({"mappings": item.mappings}),
        text=item.text,
    )

def extract_json(s: str) -> str:
    start = s.find("{")
    end = s.rfind("}")
    return s[start:end+1].strip()
    

def evaluate(item_id: int, item: DatasetItem):
    print('TEXT:', item.text)
    prompt = query_prompt(item)
    query = ask_gpt([{"role": "system", "content": prompt}], seed=item_id, temp=0)
    query = extract_json(query)
    query = json.loads(query)
    if 'query' in query:
        query = query['query']
    print('QUERY:', query)
    v = validate(item_id, item, query)
    print('RESULT:', v)


if __name__ == "__main__":
    evaluate(0, random.choice(SYHTHETIC_DATASET))
