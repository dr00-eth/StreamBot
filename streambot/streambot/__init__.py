__version__ = '1.0.2'

import requests
import json
import sseclient

class StreamBotConfig:
    def __init__(self, temperature=None, top_p=None, n=None, stop=None, max_tokens=None, presence_penalty=None, frequency_penalty=None, logit_bias=None, user=None):
        self.temperature = temperature
        self.top_p = top_p
        self.n = n
        self.stop = stop
        self.max_tokens = max_tokens
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        self.logit_bias = logit_bias
        self.user = user

class StreamBot:
    def __init__(self, api_key, bot_name, genesis_prompt, config=None, openai_url = 'https://api.openai.com/v1/chat/completions', model="gpt-3.5-turbo-0301"):
        self.api_key = api_key
        self.bot_name = bot_name
        self.config = config or StreamBotConfig()
        self.genesis_prompt = genesis_prompt
        self.messages = [{"role":"system", "content": genesis_prompt}]
        self.openai_url = openai_url
        self.model = model

    def build_req_body(self):
      req_body = {
          'model': self.model,
          'messages': self.messages,
          'stream': True
      }
  
      if self.config.temperature is not None:
        req_body['temperature'] = self.config.temperature
      if self.config.top_p is not None:
        req_body['top_p'] = self.config.top_p
      if self.config.n is not None:
        req_body['n'] = self.config.n
      if self.config.stop is not None:
        req_body['stop'] = self.config.stop
      if self.config.max_tokens is not None:
        req_body['max_tokens'] = self.config.max_tokens
      if self.config.presence_penalty is not None:
        req_body['presence_penalty'] = self.config.presence_penalty
      if self.config.frequency_penalty is not None:
        req_body['frequency_penalty'] = self.config.frequency_penalty
      if self.config.logit_bias is not None:
        req_body['logit_bias'] = self.config.logit_bias
      if self.config.user is not None:
        req_body['user'] = self.config.user
      return req_body

    def add_message(self, message, role="user"):
      self.messages.append({"role": role, "content": message})

    def chat(self, messages = []):
        reqBody = self.build_req_body()
        reqHeaders = {
            'Accept': 'text/event-stream',
            'Authorization': 'Bearer ' + self.api_key
        }
        try:
            # Fire off conversation message array to OpenAI  
            response = requests.post(self.openai_url, stream=True, headers=reqHeaders, json=reqBody)
            # Using the Server Sent Events library to support "Stream" of tokens to simulate the AI typing out
            client = sseclient.SSEClient(response)
            # Array to capture the tokens since `response` will no longer be consumable
            response_text = []
            print(self.bot_name + ": ")
            for event in client.events():
                try:
                    # Wrapped in try because json.loads fails due to `choices` not being present in last event
                    data = json.loads(event.data)['choices'][0]
                    # In first event, `delta` doesn't exist, so we check if the ['delta']['content'] keys are present
                    # Also check for ['finish_reason'] to break on last message
                    if 'delta' in data and 'content' in data['delta'] and data['finish_reason'] != 'stop':
                        response_text.append(data['delta']['content'])
                        print(data['delta']['content'], end="", flush=True)
                except json.decoder.JSONDecodeError:
                    pass
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        
        result = "".join(response_text)
      
        self.add_message(result, role="assistant")
        
        return result
