from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="New York"):
    
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&g={city}&units=imperial"
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "__main__":
    print("\n--- Weather Conditions ---")
    
    city = input("\nInput name city to get conditions: ")
    
    weeather_data = get_current_weather(city)
    print("\n")
    pprint(weeather_data)