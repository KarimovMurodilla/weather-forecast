import aiohttp
from app.config import API_KEY


class Owm:
    def __init__(self, api_key):
        self.api_key = api_key

    async def get_weather_info(self, place_name):
        async with aiohttp.ClientSession(trust_env=True) as session:
            request_url = f"http://api.openweathermap.org/data/2.5/weather?q={place_name}&appid={self.api_key}"
            async with session.get(request_url) as response:
                data = await response.json()
                return WeatherInfo(data)


class WeatherInfo:
    def __init__(self, data):
        self._data = data

    @property
    def celsius(self):
        kelvin = self._data['main']['temp']
        celsius = int(kelvin - 273.15)
        return celsius

    @property
    def wind_speed(self):
        wind_speed = self._data['wind']['speed']
        return round(wind_speed)

    @property
    def humidity(self):
        humidity = self._data['main']['humidity']
        return humidity
