import flask
import requests
from flask import jsonify
from flask import request
from config2 import api_key
from airport_func import get_city_from_ident
from airport_func import get_city_from_name

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def print_weather(weather):
    #  utility function for printing weather data received from openweathermap
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
    #  takes only relevant information from response and parses into a weather dict
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
    #  makes api call to openweathermap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    res = requests.get(complete_url)
    response = res.json()

    # as long as the server responds, parse response into weather dict
    if (response["cod"] != "404") & (response["cod"] != "400"):

        weather_dict = parse_weather(response)
        return weather_dict

    else:
        print("Error: Could not find city")
        return -1

@app.route('/', methods=['GET'])
def home():
    return "<h1>Weather API</h1><p>by Laura Joy Erb</p>"

# Default routing if no city specified
@app.route('/api/weather/all', methods=['GET'])
def api_all():
    weath = get_weather("Boston")
    if weath == -1:
        return "<h1>Error</h1><p>City could not be found</p>"
    else:
        return jsonify(weath)

# for specifying an airport with ident or airport name
@app.route('/api/weather/', methods=['GET'])
def api_ident():
    #  gets ident code or airport name from url
    if 'ident' in request.args:
        ident = request.args['ident']
        city_name = get_city_from_ident(ident)
    elif 'name' in request.args:
        name = request.args['name']
        city_name = get_city_from_name(name)
    else:
        #  executes if no fields are specified
        return "<h1>Error</h1> <p>No fields provided. Please specify either an ident code or an airport name.</p>"

    # empty string is returned if there is no matching field in the csv file
    if city_name == "":
        return "<h1>Error</h1><p>City could not be found for given ident code or airport name</p>"

    weath = get_weather(city_name)

    if weath == -1:
        return "<h1>Error</h1><p>City could not be found</p>"
    else:
        return jsonify(weath)

app.run()
