from diskcache import Cache
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


CACHE = Cache(directory=".cache")
CLIENT = OpenAI()


@CACHE.memoize()
def ask_gpt(messages: list, seed: int = 1337, temp=0.3) -> str:
    response = CLIENT.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=temp,
        frequency_penalty=0,
        presence_penalty=0,
        seed=seed,
    )
    return response.choices[0].message.content
