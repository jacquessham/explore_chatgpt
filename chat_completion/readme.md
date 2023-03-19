# Chat Completion
Chat completion is a feature to have chatbot model to return a answer from an input question.

## Set up
Before started, <b>you must upgrade the OpenAI Python Package to v0.27.0</b>. 

```
pip3 install openai --upgrade
```

## Instruction and Explanation from Documentation
Here is the example quoted from the documentation:

```
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```
<br>
In the message list, it is where you store the content of the messages among <i>system</i>, <i>user</i>, and <i>assistant</i> in dictoionaries. Conversations usually is formatted with a system message, and followed by messages between user and assistant. You may only pass a user's message, but user messages help instruct the assistant and give examples of desired behavior.
<br><br>
Quoting from the documentation:
<i>Including the conversation history helps when user instructions refer to prior messages. In the example above, the user’s final question of "Where was it played?" only makes sense in the context of the prior messages about the World Series of 2020. Because the models have no memory of past requests, all relevant information must be supplied via the conversation. If a conversation cannot fit within the model’s token limit, it will need to be shortened in some way.</i> 
<br><br>
You may run the example in <i>chat_completion_example.py</i>, the output of the example is:

```
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played at Globe Life Field in Arlington, Texas.",
        "role": "assistant"
      }
    }
  ],
  "created": 1678657493,
  "id": "chatcmpl-6tNmnNG22VkI8LlhRmzfjcGMPPijv",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 19,
    "prompt_tokens": 56,
    "total_tokens": 75
  }
}
```

## Experiment
You may find <i>who_wonf1_2021.py</i> to ask OpenAI model who won the F1 world championship.
<br><br>
Surprisingly, everytime the script runs, it produces different answers. Some of the answers are not wrong, but rather outdated. Namely, the answers I received are about 80-90% of times telling me that 2021 F1 season was not over yet, while only the rest told me it was Max Verstappen, who is the 2021 champion.
<br><br>
If we have a conversation to go over the winner for each Grand Prix, the accuracy increase significantly.
<br><br>
More detail coming soon...
