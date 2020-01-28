from typing import List, Dict
import abc


# this is an interface which will be implemented by all APIs
class Api:

    # takes in the base url that will be used for all api calls
    @abc.abstractmethod
    def __init__(self, base_url: str):
        pass
    
    # this is how the user calls the api
    # user passes in any parameters in the url, what separate the parameters, and what's between
    # the keys and values in the url
    # returns the resulting information
    @abc.abstractmethod
    def call_api(self, url_parameters: List, parameter_joiners: str, key_value_seperator: str):
        pass
    
    # this calls the actual api
    # allows for mocking the api for testing purposes
    # returns the result of the api call
    @abc.abstractmethod
    def get_info(self, url: str):
        pass

    # this takes in the api response and parses it to the format that will be returned
    # returns the relevant information from the api response
    @abc.abstractmethod
    def parse_api_response(self, api_response: Dict):
        pass

