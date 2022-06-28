from typing import NamedTuple
from pydantic import BaseModel, Field
"""
везде стоят alias потому что json приходит от openweather  с говняным неймингом
"""


class Coordinates(NamedTuple):
    """
    Отдельный класс для того, что бы было удобно обращаться к координатам
    """
    longitude: float
    latitude: float


class WeatherCondition(BaseModel):
    weather_id: int = Field(alias='id')
    sky_condition: str = Field(alias='main')
    description: str


class AirCondition(BaseModel):
    temperature: float = Field(alias='temp')
    feels_like: float
    pressure: float
    humidity: int


class SunCondition(BaseModel):
    """
    Время заката и восхода в UNIX-формате
    """
    sunrise: int
    sunset: int


class WindCondition(BaseModel):
    """
    degrees - метрологические градусы, по ним направление ветра определяется
    """
    speed: float
    degrees: int = Field(alias='deg')
    gust: float


class Weather(BaseModel):
    weather_condition: list[WeatherCondition] = Field(alias='weather')
    air_condition: AirCondition = Field(alias='main')
    sun_condition: SunCondition = Field(alias='sys')
    wind_condition: WindCondition = Field(alias='wind')
    place: str = Field(alias='name')
