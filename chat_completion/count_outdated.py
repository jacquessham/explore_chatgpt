import os
import sys
import openai


# Load token
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from load_token import *


openai.api_key = load_token()

responses = []
for _ in range(30):
  # Trigger API for response
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Who won the F1 world championship in 2021?"}

      ]
  )
  responses.append(response['choices'][0]['message']['content'])

with open('count_outdated.txt', 'w') as f:
    for response in responses:
        f.write(response)
        f.write('\n')

