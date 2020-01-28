import requests
from typing import List, Dict
import pprint as pp


import json
import weather_api


# this is a class which mocks behavior and calls to other classes or services for testing purposes
class WeatherApiMock(weather_api.WeatherApi):
    
    # mocks a real result from the api for testing purposes
    def get_info(self, url: str):
        data = None
        with open('data.txt') as json_file:
            data = json.load(json_file)
        print(type(data))
        return data;
