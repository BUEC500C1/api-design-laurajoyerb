# API Design
api-design-laurajoyerb created by GitHub Classroom
#### by Laura Joy Erb
#### Professor Osama Alshaykh
#### EC500: Building Software

### Goals
 - Develop an API and module where we can get current conditions for the airport asked by the API
 - Actively use CB and CI during development
 - Develop examples using the API

### Summary
This API receives either the four-letter identification code for an airport or the airport name. It searches through the csv file to find the record for the given airport. After the airport has been located, it returns the municipality listed for that airport. This is passed to the OpenWeatherMap API as a city name.The OpenWeatherMap API then returns current weather conditions for that city. This API returns a simplified JSON object containing the most relevant weather information for the requested airport.

###### How to Run
In your local terminal, run `python3 api.py`. The local host will start running and will direct you to go to a link.

In your browser, the welcome page will show. You can redirect to /api/weather/all to see the default page showing weather for Boston.

To search for an airport, add an ident param or a name param. For example,
  >/api/weather?ident=PABV
  
  >/api/weather?name=Birchwood Airport

### References
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://realpython.com/python-csv/#reading-csv-files-with-csv
https://www.geeksforgeeks.org/working-csv-files-python/
https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
