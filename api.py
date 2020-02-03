# Laura Joy Erb
# Professor Osama Alshaykh
# EC500: Building Software
# Project 2: API Design

import flask
import requests
import json
import csv
from flask import jsonify
from config import api_key

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#  finds airport name given an ident
def get_city_from_ident(ident):
    with open("airports.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[1] == ident:
                return row[10]
    return ""

#  finds airport name given an airport name
def get_city_from_name(airport_name):
    with open("airports.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[3] == airport_name:
                return row[10]
    return ""

def print_weather(weather):
    print("Weather for " + weather["city_name"] + ":")
    print("\tTemperature: ", end="")
    print(round(weather["temp"], 2), end="")
    print("ºC")
    print("\tFeels Like: ", end="")
    print(round(weather["feels_like"], 2), end="")
    print("ºC")
    print("\tPressure: ", end="")
    print(weather["pressure"])
    print("\tHumidity: ", end="")
    print(weather["humidity"], end="")
    print("%")
    print("\tCurrent weather status: " + weather["weather_desc"])
    print("\tWind Speed: ", end="")
    print(weather["wind_speed"])

def parse_weather(response):
    city_name = response["name"]
    feels_like = response["main"]["feels_like"]
    temperature = response["main"]["temp"]
    pressure = response["main"]["pressure"]
    humidity = response["main"]["humidity"]
    weather_description = response["weather"][0]["description"]
    wind_speed = response["wind"]["speed"]

    weather = {
        'city_name' : city_name,
        'feels_like' : round(feels_like - 273.15,2),
        'temp' : round(temperature - 273.15,2),
        'pressure' : pressure,
        'humidity' : humidity,
        'weather_desc' : weather_description,
        'wind_speed' : wind_speed
    }
    return weather

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    res = requests.get(complete_url)

    response = res.json()

    if response["cod"] != "404":

        weather_dict = parse_weather(response)
        return weather_dict

    else:
        print("Error: Could not find city")
        return -1

@app.route('/', methods=['GET'])
def home():
    return "<h1>Weather API</h1><p>by Laura Joy Erb</p>"

# Default routing if no city specified
@app.route('/api/weather', methods=['GET'])
def api():
    weath = get_weather("Boston")
    if weath == -1:
        return "<h1>Error</h1><p>City could not be found</p>"
    else:
        return jsonify(weath)

app.run()
