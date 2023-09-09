import requests
import json


API_KEY = 'ENTER YOUR API_KEY'

def get_weather(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    
    response = requests.get(base_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("Failed to fetch weather data. Check your API key or city name.")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather(city_name)
