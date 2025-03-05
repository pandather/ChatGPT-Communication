#!/usr/bin/env python3

from pydantic import BaseModel
from openai import OpenAI
import json

def load_api_key():
    with open('./api_key.json', 'r') as file:
        data = json.load(file)
        return data['api_key']
    
api_key = load_api_key()
print(api_key)

# client = OpenAI()

# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     participants: list[str]

# completion = client.beta.chat.completions.parse(
#     model="gpt-4o-2024-08-06",
#     messages=[
#         {"role": "system", "content": "Extract the event information."},
#         {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
#     ],
#     response_format=CalendarEvent,
# )

# event = completion.choices[0].message.parsed
