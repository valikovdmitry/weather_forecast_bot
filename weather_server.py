from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime


app = Flask(__name__)

# всегда пиши пинг ручка
@app.route('/')
def hello():
    return 'Hello!', 200

# add user
@app.route('/add_user', methods=['GET'])
def add_user():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di', password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    name = request.args['name']
    tg_id = request.args['tg_id']
    city = request.args['city']
    country = request.args['country']

    cursor.execute(f"SELECT * FROM service_city WHERE city_name = '{city}';")
    id_of_exist_row = cursor.fetchall()
    if id_of_exist_row:
        id_of_exist_row = id_of_exist_row[0][0]
        cursor.execute(f"""
        INSERT INTO service_user (tg_id, username,city_id) VALUES ('{tg_id}', '{name}', {id_of_exist_row});""")
    else:
        cursor.execute(f"INSERT INTO service_city (city_name, country) VALUES ('{city}', '{country}') RETURNING id;")
        id_of_new_row = cursor.fetchone()[0]
        cursor.execute(f"""
        INSERT INTO service_user (tg_id, username,city_id) VALUES ('{tg_id}', '{name}', {id_of_new_row});""")

    conn.commit()
    cursor.close()
    conn.close()

    return "User added successfully!", 200

# change city to user
@app.route('/change_city', methods=['GET'])
def change_city():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di', password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    tg_id = request.args['tg_id']
    new_city = request.args['new_city']
    country = request.args['country']

    cursor.execute(f"SELECT city_id FROM service_user WHERE tg_id = '{tg_id}';")
    old_city_id = cursor.fetchall()[0][0]

    cursor.execute(f"SELECT * FROM service_city WHERE city_name = '{new_city}';")
    if cursor.fetchall():
        cursor.execute(f"SELECT * FROM service_city WHERE city_name = '{new_city}';")
        id_ = cursor.fetchall()[0][0]
    else:
        cursor.execute(f"INSERT INTO service_city (city_name, country) VALUES ('{new_city}', '{country}') RETURNING id;")
        id_ = cursor.fetchone()[0]
    cursor.execute(f"""
        UPDATE service_user
        SET city_id = '{id_}'
        WHERE service_user.tg_id = '{tg_id}' AND city_id = '{old_city_id}';""")


    conn.commit()
    cursor.close()
    conn.close()

    return "City changed successfully!", 200

# get weather prediction
@app.route('/get_weather_prediction', methods=['GET'])
def get_weather_prediction():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di', password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    tg_id = request.args['tg_id']
    now = datetime.now().strftime('%Y-%m-%d')

    cursor.execute(f"""
    SELECT 
        forecast_date,
        forecast_time,
        weather_state_name,
        weather_state_description,
        weather_state_icon,
        the_temp,
        feels_like,
        wind_speed,
        sunrise,
        sunset,
        city_name
    FROM
        service_user
    JOIN
        service_city
    ON
        service_user.city_id = service_city.id
    JOIN
        weather
    ON
        service_user.city_id = weather.city_id
    WHERE
            service_user.tg_id = '{tg_id}'
        AND
            weather.forecast_date > '{now}'
    ;""")

    data = cursor.fetchall()

    if len(data) == 0:
        return 'You are not login.', 401

    cursor.close()
    conn.close()

    result = dict()
    names = ['morning', 'day', 'evening']

    for name, row in zip(names,data):
        result['city_name'] = row[10]
        result['forecast_date'] = row[0].strftime('%Y-%m-%d')
        result[name] = {'forecast_time': row[1].strftime('%H:%M'),
                        'weather_state_name': row[2],
                        'weather_state_description': row[3],
                        'weather_state_icon': row[4],
                        'the_temp': row[5],
                        'feels_like': row[6],
                        'wind_speed': row[7],
                        'sunrise': row[8].strftime('%H:%M'),
                        'sunset': row[9].strftime('%H:%M'),}
    return result, 200

# get sunset
@app.route('/get_sunset', methods=['GET'])
def get_sunset():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di', password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    tg_id = request.args['tg_id']
    now = datetime.now().strftime('%Y-%m-%d')

    cursor.execute(f"""
        SELECT 
            forecast_date,
            forecast_time,
            weather_state_name,
            weather_state_description,
            weather_state_icon,
            the_temp,
            feels_like,
            wind_speed,
            sunrise,
            sunset,
            city_name
        FROM
            service_user
        JOIN
            service_city
        ON
            service_user.city_id = service_city.id
        JOIN
            weather
        ON
            service_user.city_id = weather.city_id
        WHERE
                service_user.tg_id = '{tg_id}'
            AND
                weather.forecast_date >= '{now}'
        ;""")

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if len(data) == 0:
        return 'We dont know. Come back tommorow.', 404

    sunset_time = str(data[0][9])

    return sunset_time, 200

# get sunrise
@app.route('/get_sunrise', methods=['GET'])
def get_sunrise():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di',
                            password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    tg_id = request.args['tg_id']
    now = datetime.now().strftime('%Y-%m-%d')

    cursor.execute(f"""
        SELECT 
            forecast_date,
            forecast_time,
            weather_state_name,
            weather_state_description,
            weather_state_icon,
            the_temp,
            feels_like,
            wind_speed,
            sunrise,
            sunset,
            city_name
        FROM
            service_user
        JOIN
            service_city
        ON
            service_user.city_id = service_city.id
        JOIN
            weather
        ON
            service_user.city_id = weather.city_id
        WHERE
                service_user.tg_id = '{tg_id}'
            AND
                weather.forecast_date >= '{now}'
        ;""")

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if len(data) == 0:
        return 'We dont know. Come back tommorow.', 404

    sunset_time = str(data[0][8])

    return sunset_time, 200

# get all user_id
@app.route('/get_all_user_id', methods=['GET'])
def get_all_user_id():
    # connect to DB
    conn = psycopg2.connect(dbname='test_db', user='di',
                            password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    cursor.execute("SELECT tg_id FROM service_user;")

    data = cursor.fetchall()
    result = ''
    for index, user_tg_id in enumerate(data):
        if index < len(data) - 1:
            result += user_tg_id[0] + ','
        else:
            result += user_tg_id[0]

    cursor.close()
    conn.close()

    res_tupl = str(result)

    print(str(result))

    return res_tupl, 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
