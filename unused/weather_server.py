from flask import Flask
from flask import request
from flask import jsonify
import psycopg2



app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    return f'Hello, {name}!'

@app.route('/add_user', methods=['GET'])
def login():
    conn = psycopg2.connect(dbname='test_db', user='di',
                            password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    name = request.args['name']
    tg_id = request.args['tg_id']
    city = request.args['city']
    country = request.args['country']


    cursor.execute(f"INSERT INTO service_city (city_name, country) VALUES ('{city}', '{country}') RETURNING id;")
    id_of_new_row = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO service_user (tg_id, username,city_id) VALUES ('{tg_id}', '{name}', {id_of_new_row});")

    conn.commit()
    cursor.close()
    conn.close()

    print(id_of_new_row)

    return "Added", 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)