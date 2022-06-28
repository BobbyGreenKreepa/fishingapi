import pydantic.error_wrappers
import requests
from weather_api.weather_api_models import Coordinates, Weather
from weather_api.weather_api_exceptions import OpenWeatherApiServiceError

OPENWEATHER_API_KEY = '165520f5a30eed8b2d7aa80718e88ae1'
OPENWEATHER_API_URL_TEMPLATE = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}"
        "&appid=" + OPENWEATHER_API_KEY + "&lang=ru&"
                                          "units=metric"
)


def get_weather(coordinates: Coordinates) -> Weather:
    response = _get_openweather_response(coordinates)
    weather = _openweather_response_parser(response)
    return weather


def _get_openweather_response(coordinates: Coordinates) -> dict:
    try:
        openweather_response = requests.get(
            OPENWEATHER_API_URL_TEMPLATE.format(
                latitude=coordinates.latitude,
                longitude=coordinates.longitude
            )
        )
        return openweather_response.json()
    except:
        raise OpenWeatherApiServiceError


def _openweather_response_parser(openweather_response: dict) -> Weather:
    try:
        return Weather(**openweather_response)
    except pydantic.error_wrappers.ValidationError:
        raise OpenWeatherApiServiceError
