import psycopg2


def save_db(parsed):
    city_name = parsed[0]
    morning_forecast_date = parsed[1]
    morning_forecast_time = parsed[2]
    morning_weather_state_name = parsed[3]
    morning_weather_state_description = parsed[4]
    morning_weather_state_icon = parsed[5]
    morning_the_temp = parsed[6]
    morning_feels_like = parsed[7]
    morning_wind_speed = parsed[8]
    day_forecast_date = parsed[9]
    day_forecast_time = parsed[10]
    day_weather_state_name = parsed[11]
    day_weather_state_description = parsed[12]
    day_weather_state_icon = parsed[13]
    day_the_temp = parsed[14]
    day_feels_like = parsed[15]
    day_wind_speed = parsed[16]
    evening_forecast_date = parsed[17]
    evening_forecast_time = parsed[18]
    evening_weather_state_name = parsed[19]
    evening_weather_state_description = parsed[20]
    evening_weather_state_icon = parsed[21]
    evening_the_temp = parsed[22]
    evening_feels_like = parsed[23]
    evening_wind_speed = parsed[24]
    sunrise = parsed[25]
    sunset = parsed[26]

    conn = psycopg2.connect(dbname='test_db', user='di',
                            password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    # get city id
    cursor.execute(f"SELECT * FROM service_city WHERE city_name IN ('{city_name}');")
    city_id = cursor.fetchall()[0][0]

    # insert weather data
    cursor.execute(f"""
    INSERT INTO weather (
        city_id,
        forecast_date,
        forecast_time,
        weather_state_name,
        weather_state_description,
        weather_state_icon,
        the_temp,
        feels_like,
        wind_speed,
        sunrise,
        sunset
        )
    VALUES (
        '{city_id}',
        '{morning_forecast_date}',
        '{morning_forecast_time}',
        '{morning_weather_state_name}',
        '{morning_weather_state_description}',
        '{morning_weather_state_icon}',
        '{morning_the_temp}',
        '{morning_feels_like}',
        '{morning_wind_speed}',
        '{sunrise}',
        '{sunset}'
        );
    INSERT INTO weather (
        city_id,
        forecast_date,
        forecast_time,
        weather_state_name,
        weather_state_description,
        weather_state_icon,
        the_temp,
        feels_like,
        wind_speed,
        sunrise,
        sunset
        )
    VALUES (
        '{city_id}',
        '{day_forecast_date}',
        '{day_forecast_time}',
        '{day_weather_state_name}',
        '{day_weather_state_description}',
        '{day_weather_state_icon}',
        '{day_the_temp}',
        '{day_feels_like}',
        '{day_wind_speed}',
        '{sunrise}',
        '{sunset}'
        );
    INSERT INTO weather (
        city_id,
        forecast_date,
        forecast_time,
        weather_state_name,
        weather_state_description,
        weather_state_icon,
        the_temp,
        feels_like,
        wind_speed,
        sunrise,
        sunset
        )
    VALUES (
        '{city_id}',
        '{evening_forecast_date}',
        '{evening_forecast_time}',
        '{evening_weather_state_name}',
        '{evening_weather_state_description}',
        '{evening_weather_state_icon}',
        '{evening_the_temp}',
        '{evening_feels_like}',
        '{evening_wind_speed}',
        '{sunrise}',
        '{sunset}'
        )
    ;""")

    conn.commit()
    cursor.close()
    conn.close()