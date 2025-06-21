from openai import OpenAI
import os
from dotenv import load_dotenv
from .prompts import link_system_prompt, get_links_user_prompt, poem_system_prompt, get_poem_user_prompt
import json

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')


MODEL = 'gpt-4o-mini'
openai = OpenAI()

def get_links(url, links):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url, links)}
      ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

def create_poem(content,publisher):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": poem_system_prompt},
            {"role": "user", "content": get_poem_user_prompt(content, publisher)}
      ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)