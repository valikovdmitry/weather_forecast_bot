# cначала импорты внешние потом внутр(алф пор), фромы внешние потом внутр(алф пор), константы, функции
import argparse

from getter import *
from saver import *


DEFAULT_LOCATION = 'data' # глобальные переменные которые не меняются - КОНСТАНТА - пишем все апперкейсом


def get_args():
    # написать так, чтобы в мейне в функции ниче указывалось в аргументах, а писались эти аргументы


def main(city, location = DEFAULT_LOCATION):  # это скрипт
    name_woeid = get_name_woeid(city)
    wheather = get_whether(name_woeid)
    save_weather(wheather, location)


if __name__ == '__main__':
    main('san ')
