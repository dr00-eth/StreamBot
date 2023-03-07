# StreamBot
StreamBot is a Python package that allows you to create a chatbot that uses OpenAI's GPT-3 API to generate responses in real-time.

## Installation
To install StreamBot, simply run:

```shell
pip install streambot
```

## Usage
To create a StreamBot, you'll need to provide an OpenAI API key, a name for your bot, and a "genesis prompt" - the initial message that your bot will respond to.

```python
from streambot import StreamBot

api_key = "YOUR_OPENAI_API_KEY"
bot_name = "MyBot"
genesis_prompt = "Hello, how can I help you today?"

bot = StreamBot(api_key, bot_name, genesis_prompt)
Once you have created your bot, you can start chatting with it using the chat method. The chat method takes a list of messages as input and returns a string containing the bot response.
```

```python
response = bot.chat(["Hi there!", "What's your name?"])
print(response)
```

You can also add messages to your bot's message history using the add_message method.

```python
bot.add_message("Hello, how can I help you today?", role="system")
bot.add_message("Hi there!", role="user")
bot.add_message("What's your name?", role="user")
```

## Configuration
StreamBot also allows you to configure various settings for your bot, such as the temperature and maximum number of tokens used by the GPT-3 API. To do this, you can create a StreamBotConfig object and pass it to the StreamBot constructor.

```python
from streambot import StreamBot, StreamBotConfig

api_key = "YOUR_OPENAI_API_KEY"
bot_name = "MyBot"
genesis_prompt = "Hello, how can I help you today?"

config = StreamBotConfig(temperature=0.5, max_tokens=50)

bot = StreamBot(api_key, bot_name, genesis_prompt, config=config)
```

## Contributing
If you'd like to contribute to StreamBot, please feel free to submit a pull request or open an issue on the GitHub repository.

## License
StreamBot is licensed under the MIT License. See LICENSE for more information.