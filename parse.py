import json
from datetime import datetime


def json_parse(weather):
    city_name = weather['city']['name']

    # tomorrow morning weather
    morning_forecast_date = weather['list'][5]['dt_txt'][:10]
    morning_forecast_time = weather['list'][5]['dt_txt'][11:19]
    morning_weather_state_name = weather['list'][5]['weather'][0]['main']
    morning_weather_state_description = weather['list'][5]['weather'][0]['description']
    morning_weather_state_icon = weather['list'][5]['weather'][0]['icon']
    morning_the_temp = weather['list'][5]['main']['temp']
    morning_feels_like = weather['list'][5]['main']['feels_like']
    morning_wind_speed = weather['list'][5]['wind']['speed']

    # tomorrow day weather
    day_forecast_date = weather['list'][7]['dt_txt'][:10]
    day_forecast_time = weather['list'][7]['dt_txt'][11:19]
    day_weather_state_name = weather['list'][7]['weather'][0]['main']
    day_weather_state_description = weather['list'][7]['weather'][0]['description']
    day_weather_state_icon = weather['list'][7]['weather'][0]['icon']
    day_the_temp = weather['list'][7]['main']['temp']
    day_feels_like = weather['list'][7]['main']['feels_like']
    day_wind_speed = weather['list'][7]['wind']['speed']

    # tomorrow evening weather
    evening_forecast_date = weather['list'][9]['dt_txt'][:10]
    evening_forecast_time = weather['list'][9]['dt_txt'][11:19]
    evening_weather_state_name = weather['list'][9]['weather'][0]['main']
    evening_weather_state_description = weather['list'][9]['weather'][0]['description']
    evening_weather_state_icon = weather['list'][9]['weather'][0]['icon']
    evening_the_temp = weather['list'][9]['main']['temp']
    evening_feels_like = weather['list'][9]['main']['feels_like']
    evening_wind_speed = weather['list'][9]['wind']['speed']

    # converted sunrise and sunset
    sunrise_stamp = weather['city']['sunrise']
    sunrise = str(datetime.fromtimestamp(sunrise_stamp))[11:19]
    sunset_stamp = weather['city']['sunset']
    sunset = str(datetime.fromtimestamp(sunset_stamp))[11:19]

    parsed = (city_name,
              morning_forecast_date,
              morning_forecast_time,
              morning_weather_state_name,
              morning_weather_state_description,
              morning_weather_state_icon,
              morning_the_temp,
              morning_feels_like,
              morning_wind_speed,
              day_forecast_date,
              day_forecast_time,
              day_weather_state_name,
              day_weather_state_description,
              day_weather_state_icon,
              day_the_temp,
              day_feels_like,
              day_wind_speed,
              evening_forecast_date,
              evening_forecast_time,
              evening_weather_state_name,
              evening_weather_state_description,
              evening_weather_state_icon,
              evening_the_temp,
              evening_feels_like,
              evening_wind_speed,
              sunrise,
              sunset)
    return parsed

