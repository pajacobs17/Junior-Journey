from typing import List, Dict
import pprint as pp
import abc
import json


import requests


import api


# this is a class which handles behavior for the weather api
class WeatherApi(api.Api):
    
    # takes in the base url that will be used for all api calls
    def __init__(self, base_url: str):
        self._base_url = base_url

    # this is how the user calls the api
    # user passes in any parameters in the url, what separate the parameters, and what's between
    # the keys and values in the url
    # returns the resulting information
    def call_api(self, url_parameters={}, parameter_joiners='&', key_value_seperator='=') -> Dict:
        # will be used as the url for this specific api call which I will add parameters to
        api_url = self._base_url
        # for each paramater, add it apporpriately to the url
        for parameter in url_parameters:
            api_url = api_url + parameter_joiners + parameter + key_value_seperator + url_parameters[parameter]
        
        api_response = self.get_info(api_url)
        api_response = self._parse_api_response(api_response)
        
        return api_response

    # this calls the actual api
    # allows for mocking the api for testing purposes
    # returns the result of the api call
    def get_info(self, url: str) -> Dict:
        return json.loads(requests.post(url).text)
