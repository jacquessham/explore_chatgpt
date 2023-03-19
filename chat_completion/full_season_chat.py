import os
import sys
import openai
import fastf1


# Load token
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from load_token import *


openai.api_key = load_token()

# Obtain F1 event data
year = 2021
schedules = fastf1.get_event_schedule(year)['OfficialEventName']
previous_ans = []

# Trigger API for response
def add_messages(messages, schedules, previous_ans, year, world_champion=False):
	for i in range(len(previous_ans)):
		messages.append({"role": "user", "content":  f'Who won {schedules[i+1]} in {year}?'})
		messages.append({"role": "assistant", "content": previous_ans[i]})
	if world_champion:
		messages.append({"role": "user", "content":  f'Who won the F1 world champion in {year}?'})
	else:
		messages.append({"role": "user", "content":  f'Who won {schedules[len(previous_ans)+1]} in {year}?'})
	return messages

def get_response(schedules, previous_ans, event_num, year):
	messages = [{"role": "system", "content": "You are a helpful assistant."}]
	messages = add_messages(messages, schedules, previous_ans, year)
	response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages= messages
	)
	previous_ans.append(response['choices'][0]['message']['content'])
	print(response)

	return previous_ans

# Obtain answer for each Grand Prix winner
for num in range(1,len(schedules)):
	try:
		previous_ans = get_response(schedules, previous_ans, num, year)
	except:
		previous_ans.append('This API failed')


# Ask who is the F1 world champion
messages = [{"role": "system", "content": "You are a helpful assistant."}]
messages = add_messages(messages, schedules, previous_ans, year, True)
response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages= messages
)
previous_ans.append(response['choices'][0]['message']['content'])
print(response)

files = [f for f in os.listdir('.') if 'fullseason_chat' in f]


if len(files) == 0:
	filename = 'fullseason_chat_0.txt'
else:
	files.sort()
	filename = 'fullseason_chat_'+str(int(files[-1].split('.')[0][-1])+1)+'.txt'



with open(filename, 'w') as f:
    for response in previous_ans:
        f.write(response)
        f.write('\n')
