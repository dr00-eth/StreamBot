from streambot import StreamBot
import os

api_key = os.getenv("openai_key")

bot_name = 'my_bot'
bot = StreamBot(api_key, bot_name)

init_messages = {"role": "system", "content": "You are a helpful English to Spanish translation expert"}

results = bot.chat(init_messages)

print(results)