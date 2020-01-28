# this module is a unified interface for the api calling program
import pprint as pp


import invalid_menu_option as imo
import weather_api_forecast
import weather_api_current


class ApiWrapper:

    def run(self):
        keepGoing = True

        # menu will keep going until the user exits it
        while(keepGoing):
            # print out options and catch user input
            print('Welcome to my program. Please enter the number of the API you would like to work with')
            print('1. Weather related api')
            print('2. Exit')
            api = input()
            
            # control structure for the specific api to call depending upon user input
            if(api == '1'):
                self.weather_menu()            
            elif(api == '2'):
                keepGoing = False
            else:
                raise imo.InvalidMenuOptionException('Invalid input provided')

    def weather_menu(self):
        api_resp = None

        # print out options and catch user input
        print('Welcome to my program. Please enter the number of the API you would like to work with')
        print('1. 5 day forecast')
        print('2. Current weather')
        api = input()
        
        # control structure for the specific api to call depending upon user input
        # if either api is called then ask for user input for location and then create the appropriate obj
        if(api == '1' or api =='2'):
            # contains all the url parameters that will be placed in key-value format with the keys in the dict
            # being the keys used in the API request
            url_parameters = {}
            # create weather obj pointer and take in the location information
            weather_obj = None
            zipcode = input('Please enter the zip code of the location you wnat.')
            country_code = input('Please enter the country code of the zip code. If one is not provided, us will be used.')
            # country code is expected in lowercase
            country_code = country_code.lower()
            
            # adds zipcode in format expected to the url parameters            
            url_parameters['zip'] = zipcode + ',' + country_code
            # create the approrpriate object and call its' api and print the response
            if(api =='1'):
                weather_obj = self.get_weather_api_forecast_obj('http://api.openweathermap.org/data/2.5/forecast?APPID=39f3e821db5677389a039e95b1b33ba0')
            else:
                weather_obj = self.get_weather_api_current_obj('http://api.openweathermap.org/data/2.5/weather?APPID=39f3e821db5677389a039e95b1b33ba0');
            api_resp = weather_obj.call_api(url_parameters)
            pp.pprint(api_resp)
        else:
            raise imo.InvalidMenuOptionException('The menu option you entered was invalid')

    def get_weather_api_forecast_obj(self, url):
        return weather_api_forecast.WeatherApiForecast(url)

    def get_weather_api_current_obj(self, url):
        return weather_api_current.WeatherApiCurrent(url)
