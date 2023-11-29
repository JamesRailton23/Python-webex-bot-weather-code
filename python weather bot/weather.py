from webex_bot.models.command import Command
import logging
import requests
import json

log = logging.getLogger(__name__)


class WeatherByZIP(Command):
    def __init__(self):
        super().__init__(
            command_keyword="weather",
            help_message="Get current weather conditions by post code.",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):

        zip_code = message.strip()

        # Define our URL, with requested ZIP code & API Key
        APIkey = 
        url = "https://api.openweathermap.org/data/2.5/weather?"
        url += f"zip={zip_code},GB&units=metric&appid={APIkey}"

        # Query weather
        response = requests.get(url)
        weather = response.json()

        # Pull out desired info

        city = weather["name"]
        conditions = weather["weather"][0]["description"]
        temperature = weather["main"]["temp"]
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]

        response_message = (
            f"In {city}, it's currently {temperature}*c with {conditions}. "
        )
        response_message += f"Wind speed is {wind}mph. Humidity is {humidity}%"

        return response_message
