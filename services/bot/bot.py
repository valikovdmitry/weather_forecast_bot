import requests
import logging
import asyncio
import aioschedule
import json
from aiogram import Bot, Dispatcher, executor, types
from timezone_dict import timezone_id_vs_sending_time
from datetime import datetime, timedelta, timezone

HOST = '0.0.0.0'
PORT = 5000
API_KEY_OPENWEATHER = "7cd5dc8b0ff00c17b7bd39ee80c7a615"

bot = Bot(token="5479483561:AAEI8Rn9-MFXvxegkTX8r9Llt252iz69pII")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("""
    Каждые сутки Пашок пришлет вам погоду в 20:00 по Москве.
    
    /set_city - задать город
    /change_city - изменить город
    /sunset - когда закат
    /sunrise - когда восход
    """)


@dp.message_handler(commands="set_city")
async def set_city(message: types.Message):
    if ',' in message.text:
        city, country = message.text.split(',')
        city = city.replace('/set_city ', '')
        response = requests.get('http://127.0.0.1:5000/add_user',
                                params={"name": message.from_user.first_name,
                                        "tg_id": message.from_user.id,
                                        "city": city,
                                        "country": country
                                        })
        if response.status_code == 200:
            await message.answer('Пользователь добавлен успешно!')
        else:
            await message.answer('Ошибка при добавлении!')
    else:
        await message.answer('Напиши команду в формате \"/set_city Moscow,RU\"!')


@dp.message_handler(commands="change_city")
async def change_city(message: types.Message):
    if ',' in message.text:
        city, country = message.text.split(',')
        city = city.replace('/change_city ', '')
        response = requests.get('http://127.0.0.1:5000/change_city',
                                params={"tg_id": message.from_user.id,
                                        "new_city": city,
                                        "country": country
                                        })
        if response.status_code == 200:
            await message.answer('Город сменен успешно!')
        else:
            await message.answer('Ошибка при смене города!')
    else:
        await message.answer('Напиши команду в формате \"/change_city Moscow,RU\"!')


async def get_weather_prediction(tg_id):
    response = requests.get('http://127.0.0.1:5000/get_weather_prediction', params={"tg_id": tg_id})
    result = json.loads(response.text)

    city_name = result['city_name']
    morning_weather_state_name = result['morning']['weather_state_name']
    morning_the_temp = result['morning']['the_temp']
    if morning_the_temp > 0:
        morning_the_temp = f'+ {morning_the_temp}'
    day_weather_state_name = result['day']['weather_state_name']
    day_the_temp = result['day']['the_temp']
    if day_the_temp > 0:
        day_the_temp = f'+ {day_the_temp}'
    evening_weather_state_name = result['evening']['weather_state_name']
    evening_the_temp = result['evening']['the_temp']
    if evening_the_temp > 0:
        evening_the_temp = f'+ {evening_the_temp}'

    formated = f"""{city_name}\n
Morning : {str(morning_the_temp)} // {morning_weather_state_name}\n
Day: {str(day_the_temp)} // {day_weather_state_name}\n
Evening: {str(evening_the_temp)} // {evening_weather_state_name}\n"""

    await bot.send_message(tg_id, formated)


async def get_weather_prediction_now(city_name, tg_id, timezone_name):
    weather_response = requests.get('https://api.openweathermap.org/data/2.5/forecast',
                                    params={"q": f"{city_name}", "cnt": 12, "appid": f"{API_KEY_OPENWEATHER}",
                                            "units": "metric"})
    weather = weather_response.json()
    city_name = weather['city']['name']

    # offset and timezone
    offset = timedelta(hours=timezone_name)
    tz = timezone(offset)

    # tomorrow morning time
    morning_forecast_date = weather['list'][5]['dt_txt'][:10]
    morning_forecast_time = weather['list'][4]['dt_txt'][11:19]

    # tomorrow morning weather
    morning_weather_state_name = weather['list'][4]['weather'][0]['main']
    morning_the_temp = weather['list'][4]['main']['temp']

    # tomorrow day time
    day_forecast_time = weather['list'][6]['dt_txt'][11:19]

    # tomorrow day weather
    day_weather_state_name = weather['list'][6]['weather'][0]['main']
    day_the_temp = weather['list'][6]['main']['temp']

    # tomorrow evening time
    evening_forecast_time = weather['list'][8]['dt_txt'][11:19]

    # tomorrow evening weather
    evening_weather_state_name = weather['list'][8]['weather'][0]['main']
    evening_the_temp = weather['list'][8]['main']['temp']


    # converted sunset
    sunset_stamp = weather['city']['sunset']
    sunset = datetime.fromtimestamp(sunset_stamp, tz=tz)
    tz.utcoffset(sunset)

    # converted sunrise
    sunrise_stamp = weather['city']['sunrise']
    sunrise = datetime.fromtimestamp(sunrise_stamp, tz=tz)
    tz.utcoffset(sunrise)

    base = weather['city']

    formated = f"""
{city_name}\n
Morning : {str(morning_the_temp)} // {morning_weather_state_name}\n
Day: {str(day_the_temp)} // {day_weather_state_name}\n
Evening: {str(evening_the_temp)} // {evening_weather_state_name}\n\n
Sunrise: {sunrise.strftime('%H:%M')}\n
Sunset: {sunset.strftime('%H:%M')}
"""

    await bot.send_message(tg_id, formated)


async def noon_print():
    now_time = str(int(datetime.now().strftime('%H')) + 0)
    now_time_w_sec = datetime.now().strftime('%H:%M:%S')
    print(now_time_w_sec)
    print('now_time = ', now_time)

    for key, value in timezone_id_vs_sending_time.items():
        if value[0] == now_time:
            timezone_id = key
            timezone_name = value[1]
    print('timezone_id = ', timezone_id)
    print('timezone_name = ', timezone_name)

    needed_city = requests.get('http://127.0.0.1:5000/get_needed_city_name',
                               params={'timezone_id': timezone_id}).text
    print('needed_city = ', needed_city)


    if needed_city == 'Not found':
        print('No users for that time zone.')
        pass
    else:
        needed_json = json.loads(needed_city)
        for i in needed_json:
            print(i, needed_json[i])
            if len(needed_json[i]) > 1:
                for v in needed_json[i]:
                    print('В работу пошла - ', i, v)
                    await get_weather_prediction_now(i, v, timezone_name)
            else:
                print('В работу пошла - ', i, needed_json[i][0])
                await get_weather_prediction_now(i, needed_json[i][0], timezone_name)




async def scheduler():
    # aioschedule.every().day.at("20:00").do(noon_print)
    # aioschedule.every().hour.do(noon_print)
    aioschedule.every().hour.at(":00").do(noon_print)
    # aioschedule.every(0.1).minutes.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
