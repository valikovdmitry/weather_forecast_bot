import argparse

def get_args():
    # написать так, чтобы в мейне в функции ниче указывалось в аргументах, а писались эти аргументы
    parser = argparse.ArgumentParser(description='I will save weather for your city.')
    parser.add_argument('city', type=str, help='Type a city.')
    parser.add_argument('-dir', type=str, default='data', help='Type an optional dir where to save weather. (default dir is /data/)')
    args = parser.parse_args()
    city = args.city
    dir = args.dir

    return city, dir


