# Setup

## First time
Download the API key first. Then, set up a Python enviornment with following command:

```
python -m venv explore_chatgpt
. explore_chatgpt/bin/activate
pip install -r requirements.txt
```
<br>
All Python dependencies, including <i>OpenAI</i> will be installed in this command.
<br><br>
Note: <i>requirements.txt</i> can be found in the <a href="https://github.com/openai/openai-quickstart-python">OpenAI Quickstart repository</a>.
<br><br>

## Instruction
After you have setup, you may use the followed commands to activate the environment.

```
. explore_chatgpt/bin/activate
```
Then, you can run your scripts with ChatGPT.
<br><br>
Once you are done, deactivate with the following:

```
deactivate
```

## Loading OpenAI Token
You may find <i>load_token.py</i> to help setup the OpenAI token in the parent directory. You may save a file named <i>openai_token.json</i> in your local Desktop with only one field <i>openai_token</i> with the value of your OpenAI token. In each execution script across all subfolders in this repository, you may find the following code to import:

```
# Load token
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from load_token import *


openai.api_key = load_token()
```
<br>
No input is needed to the funtion <i>load_token()</i>, therefore, be sure to follow the format below for the JSON file and saved in the local Desktop:

```
{
	"openai_token":<OpenAI_token>
}
```