from weather import WeatherByZIP

from webex_bot.commands.echo import EchoCommand
from webex_bot.commands.help import HelpCommand

from webex_bot.webex_bot import WebexBot


bot = WebexBot(
    teams_bot_token=(
        
    ),
    include_demo_commands=True,
)


bot.add_command(EchoCommand())
bot.add_command(WeatherByZIP())
bot.add_command(
    HelpCommand(
        bot_name="wexbot",
        bot_help_subtitle="",
        bot_help_image="https://i.postimg.cc/2jMv5kqt/AS89975.jpg",
    )
)

# Call `run` for the bot to wait for incoming messages.
bot.run()
