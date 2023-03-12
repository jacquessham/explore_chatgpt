# Obtained from Documentation
## https://platform.openai.com/docs/guides/chat/introduction

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import sys
import os

# Load token
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from load_token import *


openai.api_key = load_token()
   
# Make API call to trigger the chat completion
response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Who won the world series in 2020?"},
                    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                    {"role": "user", "content": "Where was it played?"}
                ]
            )
print(response)