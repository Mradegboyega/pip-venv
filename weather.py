import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Your Current Weather Condition ***\n")

    city = input("\nKindly enter your city:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    try:
        print(f"\nCurrent weather for {weather_data['name']}")
        print(f"\nThe temperature is {weather_data['main']['temp']}°C")
        print(f"\nFeels like {weather_data['main']['feels_like']}°C and {weather_data['weather'][0]['description']}.")

    except KeyError as e:
        print(f"Error: {e}. Please check your city name and try again.")

if __name__ == "__main__":
    get_current_weather()
