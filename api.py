# Laura Joy Erb
# Professor Osama Alshaykh
# EC500: Building Software
# Project 2: API Design

# import required modules
import requests
import json
from config import api_key

def print_weather(response):

    city_name = response["name"]
    feels_like = response["main"]["feels_like"]
    temperature = response["main"]["temp"]
    pressure = response["main"]["pressure"]
    humidity = response["main"]["humidity"]
    weather_description = response["weather"][0]["description"]
    wind_speed = response["wind"]["speed"]

    print("Weather for " + city_name + ":")
    print("\tTemperature: ", end="")
    print(round(temperature - 273.15, 2), end="")
    print("ºC")
    print("\tFeels Like: ", end="")
    print(round(feels_like - 273.15, 2), end="")
    print("ºC")
    print("\tPressure: ", end="")
    print(pressure)
    print("\tHumidity: ", end="")
    print(humidity, end="")
    print("%")
    print("\tCurrent weather status: " + weather_description)
    print("\tWind Speed: ", end="")
    print(wind_speed)

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    res = requests.get(complete_url)

    response = res.json()

    if response["cod"] != "404":

        print_weather(response)
        return 0

    else:
        print("Error: Could not find city")
        return -1

get_weather("Boston")
