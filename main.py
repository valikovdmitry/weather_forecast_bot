# cначала импорты внешние потом внутр(алф пор), фромы внешние потом внутр(алф пор), константы, функции
from get import *
from parse import *
from save import *
from find import *


API_KEY_OPENWEATHER = "7cd5dc8b0ff00c17b7bd39ee80c7a615"


def main(city):  # это скрипт
    wheather = get_whether(city)
    parsed = json_parse(wheather)
    save_db(parsed)
    print('Sucsess!')


if __name__ == '__main__':
    cities = requested()
    for city in cities:
        main(city)
