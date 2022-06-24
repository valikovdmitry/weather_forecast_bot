import requests
import logging
import asyncio
import aioschedule
import json
from aiogram import Bot, Dispatcher, executor, types


HOST = '127.0.0.1'
PORT = 5000

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


async def noon_print():
    response = requests.get('http://127.0.0.1:5000/get_all_user_id').text.split(',')
    for id in response:
        await get_weather_prediction(id)


async def scheduler():
    aioschedule.every().day.at("20:00").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
