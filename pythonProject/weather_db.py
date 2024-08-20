
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float, UniqueConstraint
from sqlalchemy.orm import sessionmaker

Base = sqlalchemy.orm.declarative_base()


class WeatherRecord(Base):
    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    sum_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

    __table_args__ = (
        UniqueConstraint('latitude', 'longitude', 'month', 'day', 'year', name='_location_date_uc'),
    )

    def __repr__(self):
        return (f"<WeatherRecord(id={self.id}, latitude={self.latitude}, longitude={self.longitude}, "
                f"date={self.year}-{self.month:02d}-{self.day:02d}, avg_temp={self.avg_temp}, "
                f"min_temp={self.min_temp}, max_temp={self.max_temp}, avg_wind_speed={self.avg_wind_speed}, "
                f"min_wind_speed={self.min_wind_speed}, max_wind_speed={self.max_wind_speed}, "
                f"sum_precipitation={self.sum_precipitation}, min_precipitation={self.min_precipitation}, "
                f"max_precipitation={self.max_precipitation})>")


def init_db():
    engine = create_engine('sqlite:///weather.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


Session = init_db()



def save_weather_data(weather_data, session=None):
    close_session = False
    if session is None:
        Session = init_db()
        session = Session()
        close_session = True

    # Check if a record exists
    record = session.query(WeatherRecord).filter_by(
        latitude=weather_data.latitude,
        longitude=weather_data.longitude,
        month=weather_data.month,
        day=weather_data.day,
        year=weather_data.year
    ).first()

    if record:
        # Update the existing record
        record.avg_temp = weather_data.avg_temp
        record.min_temp = weather_data.min_temp
        record.max_temp = weather_data.max_temp
        record.avg_wind_speed = weather_data.avg_wind_speed
        record.min_wind_speed = weather_data.min_wind_speed
        record.max_wind_speed = weather_data.max_wind_speed
        record.sum_precipitation = weather_data.sum_precipitation
        record.min_precipitation = weather_data.min_precipitation
        record.max_precipitation = weather_data.max_precipitation
    else:
        # Insert a new record
        record = WeatherRecord(
            latitude=weather_data.latitude,
            longitude=weather_data.longitude,
            month=weather_data.month,
            day=weather_data.day,
            year=weather_data.year,
            avg_temp=weather_data.avg_temp,
            min_temp=weather_data.min_temp,
            max_temp=weather_data.max_temp,
            avg_wind_speed=weather_data.avg_wind_speed,
            min_wind_speed=weather_data.min_wind_speed,
            max_wind_speed=weather_data.max_wind_speed,
            sum_precipitation=weather_data.sum_precipitation,
            min_precipitation=weather_data.min_precipitation,
            max_precipitation=weather_data.max_precipitation
        )
        session.add(record)

    session.commit()
    if close_session:
        session.close()

def get_weather_data(latitude, longitude, month, day, year):
    session = Session()
    records = session.query(WeatherRecord).filter_by(
        latitude=latitude, longitude=longitude, month=month, day=day, year=year).all()
    session.close()
    return records
