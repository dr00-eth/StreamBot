# StreamBot
StreamBot is a Python package that allows you to create a chatbot that uses OpenAI's GPT-3 API to generate responses in real-time.

## Installation
To install StreamBot, simply run:

```shell
pip install streambot
```

## Usage
To create a StreamBot, you'll need to provide an OpenAI API key, a name for your bot, and a "genesis prompt" - the initial `system` message that your bot will act like.

```python
from streambot import StreamBot

api_key = "YOUR_OPENAI_API_KEY"
bot_name = "MyBot"
genesis_prompt = "You are a helpful English to Spanish translator"

bot = StreamBot(api_key, bot_name, genesis_prompt)
```

Once you have created your bot, you can initiate output with the chat method. The chat method takes a list of messages managed within the StreamBot class as input and prints the stream of tokens as well as optionally returning a string containing the bot response into a variable.

The StreamBot constructor takes in an optional OpenAI URL (in case they change it) and an override for the Model value as they may change that in the near future as well. Also see below for additional configuration overrides as part of the StreamBotConfig you can pass in.


```python
prompt = input("Me: ")
bot.add_message(prompt)
bot.chat()
```

You can also add messages to your bot's message history using the add_message method. The add_message method defaults the role to "user" if none is provided.

```python
bot.add_message("Hello, how can I help you today?", role="assistant")
bot.add_message("Hi there!")
bot.add_message("What's your name?", role="assistant")
```

## Configuration
StreamBot also allows you to configure various settings for your bot, such as the temperature and maximum number of tokens used by the GPT-3 API. To do this, you can create a StreamBotConfig object and pass it to the StreamBot constructor.

```python
from streambot import StreamBot, StreamBotConfig

api_key = "YOUR_OPENAI_API_KEY"
bot_name = "MyBot"
genesis_prompt = "Hello, how can I help you today?"

config = StreamBotConfig(temperature=0.5, max_tokens=500)

bot = StreamBot(api_key, bot_name, genesis_prompt, config=config)
```

## Contributing
If you'd like to contribute to StreamBot, please feel free to submit a pull request or open an issue on the GitHub repository.

## License
StreamBot is licensed under the MIT License. See LICENSE for more information.