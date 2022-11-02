import requests, json
from app.config import API_KEY


class Owm:
    def __init__(self, api_key):
        self.api_key = api_key


    def get_weather_info(self, place_name):
        return WeatherInfo(self.api_key, place_name)


class WeatherInfo(Owm):
    def __init__(self, api_key, place_name):
        self.api_key = api_key
        self.place_name = place_name

        self.celsius = self.get_celsius()
        self.wind_speed = self.get_wind_speed()
        self.humidity = self.get_humidity()


    def get_full_weather_info(self) -> dict:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + self.api_key + "&q=" + self.place_name
        self.response = requests.get(complete_url)
        
        return self.response.json()


    def get_celsius(self):
        kalvin = self.get_full_weather_info().get('main').get('temp')
        celsius = int(kalvin - 273.15)
        
        return celsius

    
    def get_wind_speed(self):
        wind_speed = self.get_full_weather_info().get('wind').get('speed')

        return round(wind_speed)


    def get_humidity(self):
        humidity = self.get_full_weather_info().get('main').get('humidity')

        return humidity