import re
import subprocess
from functools import cache
from typing import List, Optional

from dataset import DatasetItem
from llms import ask_gpt
from synthetic import SYHTHETIC_DATASET
from validation import ValidationResult, validate

GEN_PROMPT = """
You are an AI designed to help with creating a dataset for text to ElasticSearch query LLM fine tuning.

Here is the seed dataset you should use for generating more examples:
```python
{dataset}
```

Here are some ideas for generating more examples:

* Add noise to the index definition to teach the model to pick the right fields.
* Use diverse property names.
* Use diverse business domains (finance, sales, retail, production, etc).
* Cover the following data types: `text`, `keyword`, `integer`, `date`, `boolean`.
* Have more than one document for positive (include) and negative (exclude) examples.
* Clarification should reflect thought process and will only be used during training.
* Use date functions to calculate relative dates in the query.
* Difficulty level: hard.
* Focus area: relative date ranges.

Generate more examples to cover as much query synthax as possible. Output Python list and nothing more.

Output format:
```python
[
    DatasetItem(...),
    DatasetItem(...),
    ...
]
```
""".strip()

FIX_PROMPT = """
There was an error during validation of the generated example:
```
{error}
```

Fix the example and reply with the corrected Python code. 

Output format:
```python
DatasetItem(...)
```
"""


@cache
def gen_prompt():
    ds = open("dataset.py").read()
    prompt = GEN_PROMPT.format(dataset=ds)
    return prompt


def fix_prompt(error: str):
    return FIX_PROMPT.format(error=error)


def assistant_content(item: DatasetItem) -> str:
    return f"```python\n{repr([item])}\n```"


def generate(seed: int) -> List[DatasetItem]:
    items = ask_gpt([{"role": "system", "content": gen_prompt()}], seed, temp=0.5)
    items = extract_code(items)
    items = eval(items)
    return items


def extract_code(text: str) -> str:
    return re.search(r"```python\n(.*?)```", text, re.DOTALL).group(1).strip()


def fix(
    item: DatasetItem, v: ValidationResult, attempts: int = 3
) -> Optional[DatasetItem]:
    messages = [
        {"role": "system", "content": gen_prompt()},
        {"role": "assistant", "content": assistant_content(item)},
        {"role": "user", "content": fix_prompt(repr(v))},
    ]
    fixed = ask_gpt(messages, seed=attempts, temp=0.5)
    fixed = extract_code(fixed)
    fixed = eval(fixed)

    v = validate(0, fixed, fixed.query)

    if v.status == "error":
        if fixed == item:
            print("Failed to fix example, it's the same as before")
            return None
        if attempts > 0:
            print(f"Failed to fix example: {v.reason}, trying again")
            return fix(fixed, v, attempts - 1)
        else:
            return None

    return fixed


def save(items: List[DatasetItem]):
    items = SYHTHETIC_DATASET + items

    def deduped():
        seen = set()
        for item in items:
            if item.text not in seen:
                seen.add(item.text)
                yield item

    items = list(deduped())

    out_file = "synthetic.py"

    with open(out_file, "w") as f:
        f.write("from dataset import DatasetItem\n\n")
        f.write(f"SYHTHETIC_DATASET = {repr(items)}")

    print(f"Saved {len(items)} total items to {out_file}")

    subprocess.run(["black", out_file])  # format file with black


def main():
    items = generate(12)
    valid = []
    for item_id, item in enumerate(items):
        v = validate(item_id, item, item.query)
        if v.status == "ok":
            valid.append(item)
        elif v.status == "error":
            print("Trying to fix invalid example")
            item = fix(item, v)
            if item is not None:
                print("Fixed invalid example")
                valid.append(item)
            else:
                print("Giving up invalid example")

    print(f"Generated {len(items)} examples, {len(valid)} are valid")

    save(valid)


if __name__ == "__main__":
    main()
