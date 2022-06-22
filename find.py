import psycopg2


def requested():
    conn = psycopg2.connect(dbname='test_db', user='di',
                            password='1111', host='192.168.1.100', port=5432)
    cursor = conn.cursor()

    # get city id
    cursor.execute(f"SELECT city_name FROM service_city;")
    all_cities = cursor.fetchall()
    requested_cities = []
    for city in all_cities:
        requested_cities.append(city[0])

    return requested_cities
