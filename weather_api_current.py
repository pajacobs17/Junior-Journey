from typing import List, Dict


import weather_api


# this is a class which handles behavior for the current weather api
class WeatherApiCurrent(weather_api.WeatherApi):

    # handles specific behavior for formatting of the forecast response data
    # takes in the response from the api in a json Dict
    # returns the modified dict
    def _parse_api_response(self, api_response: Dict) -> Dict:
        limited_resp = api_response.get('weather', {})[0]
        limited_resp.pop('id', None)
        limited_resp.pop('icon', None)

        return limited_resp
