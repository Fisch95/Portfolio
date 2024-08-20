# Import class from weather_project
from weather_db import save_weather_data, get_weather_data
from weather_project import WeatherData

# Define main and the required variables
def main():
    latitude = 41.1306
    longitude = -85.1289
    month = 5
    day = 3
    year = 2024

    weather = WeatherData(latitude, longitude, month, day, year)
    weather.fetch_weather_data(year)

    save_weather_data(weather) # Saves data to database

    print(f"Mean Temperature: {weather.get_mean_temperature()} °F")
    print(f"Maximum Wind Speed: {weather.get_maximum_wind_speed()} mph")
    print(f"Precipitation Sum: {weather.get_precipitation_sum()} inches")

    records = get_weather_data(latitude, longitude, month, day, year)
    for record in records:
        print(record)

# Method to query the table within the database
def display_weather_data(latitude, longitude, month, day, year):
    records = get_weather_data(latitude, longitude, month, day, year)
    for record in records:
        print(record)



if __name__ == "__main__":
    main()

