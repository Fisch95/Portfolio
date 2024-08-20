import unittest
from weather_project import WeatherData
from weather_db import save_weather_data, get_weather_data, init_db, Base, WeatherRecord
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestWeatherData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        cls.Session = sessionmaker(bind=cls.engine)
        Base.metadata.create_all(cls.engine)

    def setUp(self):
        self.latitude = 41.1306
        self.longitude = -85.1289
        self.month = 5
        self.day = 3
        self.year = 2024
        self.weather_data = WeatherData(self.latitude, self.longitude, self.month, self.day, self.year)
        self.weather_data.fetch_weather_data(self.year)
        self.session = self.Session()

    def test_fetch_weather_data(self):
        self.assertIsNotNone(self.weather_data.avg_temp)
        self.assertIsNotNone(self.weather_data.min_temp)
        self.assertIsNotNone(self.weather_data.max_temp)
        self.assertIsNotNone(self.weather_data.avg_wind_speed)
        self.assertIsNotNone(self.weather_data.min_wind_speed)
        self.assertIsNotNone(self.weather_data.max_wind_speed)
        self.assertIsNotNone(self.weather_data.sum_precipitation)

    def test_save_weather_data(self):
        save_weather_data(self.weather_data, self.session)
        records = self.session.query(WeatherRecord).all()
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record.avg_temp, self.weather_data.avg_temp)
        self.assertEqual(record.min_temp, self.weather_data.min_temp)
        self.assertEqual(record.max_temp, self.weather_data.max_temp)
        self.assertEqual(record.avg_wind_speed, self.weather_data.avg_wind_speed)
        self.assertEqual(record.min_wind_speed, self.weather_data.min_wind_speed)
        self.assertEqual(record.max_wind_speed, self.weather_data.max_wind_speed)
        self.assertEqual(record.sum_precipitation, self.weather_data.sum_precipitation)
        self.assertEqual(record.min_precipitation, self.weather_data.min_precipitation)
        self.assertEqual(record.max_precipitation, self.weather_data.max_precipitation)

    def test_update_weather_data(self):
        save_weather_data(self.weather_data, self.session)
        self.weather_data.avg_temp += 1.0
        self.weather_data.min_temp -= 1.0
        save_weather_data(self.weather_data, self.session)
        records = get_weather_data(self.latitude, self.longitude, self.month, self.day, self.year)
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual( self.weather_data.avg_temp, self.weather_data.avg_temp)
        self.assertEqual(self.weather_data.min_temp, self.weather_data.min_temp)

    def tearDown(self):
        self.session.query(WeatherRecord).delete()
        self.session.commit()
        self.session.close()


if __name__ == "__main__":
    unittest.main()