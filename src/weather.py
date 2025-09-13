import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions \n***")
    
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            print("API key not found!")
            return
        
        city = input("Please enter your city:\n")

        request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(request_url)

        response.raise_for_status()

        weather_data = response.json()
        # pprint(weather_data)  # full json

        print(f"\nCurrent weather for {weather_data["name"]}:::")
        print(f"\nThe Temp is {weather_data["main"]["temp"]:.1f}")

    except Exception as err:
        print(f"An unexpected error occurred::: {err}")

get_current_weather()

