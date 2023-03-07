from streambot import StreamBot, StreamBotConfig
import os

api_key = os.getenv("openai_key")
bot_name = 'my_bot'

config = StreamBotConfig(temperature=0.33, top_p=0.1, n=5, stop=1, max_tokens=10, presence_penalty=0.1, frequency_penalty=0.1, user='some user', logit_bias=None)

bot = StreamBot(api_key, bot_name, genesis_prompt="You are a helpful English to Spanish translation expert.", config=config)

results = bot.chat()

while True:
  user_input = input("Me: ")
  
  bot.add_message(user_input)
  
  response = bot.chat()

  bot.add_message(response, role="assistant")