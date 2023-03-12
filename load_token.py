import os
import json


def load_token():
    # Obtain OpenAI token
    try:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    except:
        print('Please adjust the token file path')
        quit()
    return json.load(open(desktop+'/openai_token.json'))['openai_token']