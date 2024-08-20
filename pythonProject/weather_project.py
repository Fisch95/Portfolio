# import necessary packages for project function
import requests


# Create a class to process data from the api
class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = sum(self.get_mean_temperature()) / len(self.get_mean_temperature())
        self.min_temp = min(self.get_mean_temperature())
        self.max_temp = max(self.get_mean_temperature())
        self.avg_wind_speed = sum(self.get_maximum_wind_speed()) / len(self.get_maximum_wind_speed())
        self.min_wind_speed = min(self.get_maximum_wind_speed())
        self.max_wind_speed = max(self.get_maximum_wind_speed())
        self.sum_precipitation = sum(self.get_precipitation_sum())
        self.min_precipitation = min(self.get_precipitation_sum())
        self.max_precipitation = max(self.get_precipitation_sum())


# Function to call the API
    def fetch_weather_data(self, year):
        start_date = f"{year}-{self.month:02d}-{self.day:02d}"
        end_date = f"{year}-{self.month:02d}-{self.day:02d}"

        url = f"https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["daily"]
            return {
                'avg_temp': data['temperature_2m_mean'][0],
                'max_wind_speed': data['wind_speed_10m_max'][0],
                'sum_precipitation': data['precipitation_sum'][0]
            }
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None


# Methods for the specific data required for the project
    def get_mean_temperature(self):
        mean_temps = []
        for year in range(self.year - 4, self.year + 1):
            data = self.fetch_weather_data(year)
            if data:
                mean_temps.append(data['avg_temp'])
        return mean_temps


    def get_maximum_wind_speed(self):
        wind_speeds = []
        for year in range(self.year - 4, self.year + 1):
            data = self.fetch_weather_data(year)
            if data:
                wind_speeds.append(data['max_wind_speed'])
        return wind_speeds


    def get_precipitation_sum(self):
        precipitation = []
        for year in range(self.year - 4, self.year + 1):
            data = self.fetch_weather_data(year)
            if data:
                precipitation.append(data['sum_precipitation'])
        return precipitation
