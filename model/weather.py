class Weather:
    
    def __init__(self, weather_data: dict):
        self._weather_data = weather_data

    @property
    def country(self):
        return self._weather_data['sys']['country']
   
    @property 
    def city(self):
        return self._weather_data['name']
    
    @property
    def temp_min(self):
        return self.kelvin_to_celsius(self._weather_data['main']['temp_min'])

    @property
    def temp_max(self):
        return self.kelvin_to_celsius(self._weather_data['main']['temp_max'])

    @property
    def description(self):
        return self._weather_data['weather'][0]['description']
    
    @property
    def humidity(self):
        return self._weather_data['main']['humidity']
    
    @property
    def icon(self):
        return self._weather_data['weather'][0]['icon']

    def kelvin_to_celsius(self, temperature: float):
        return round(temperature - 273.15,2)