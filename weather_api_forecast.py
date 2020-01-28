
from typing import List, Dict
import pprint as pp


import weather_api


# this is a class which handles behavior for the forecast weather api
class WeatherApiForecast(weather_api.WeatherApi):
    
    # handles specific behavior for formatting of the forecast response data
    # takes in the response from the api in a json Dict
    # returns the modified dict
    def _parse_api_response(self, api_response: Dict) -> Dict:
        forecasts = api_response.get('list', [])
        i = 0
        daily_forecasts = []
        # grab a daily forecast by getting 1 forecast for each day
        while i < len(forecasts):
            day = {forecasts[i]['dt_txt']: [forecasts[i]['weather'], forecasts[i]['main']]}
            daily_forecasts.append(day)
            # 8 was chosen as the api returns data for every 3 hours (8 per day)
            i += 8

        return daily_forecasts
