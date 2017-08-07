import json
from math import sqrt
import operator
import os
import sys


def calc_distance(longitude_from, latitude_from, longitude_to, latitude_to):
    return sqrt(
                (pow((longitude_from - longitude_to), 2) +
                 pow((latitude_from - latitude_to), 2)),
                )


def get_biggest_bar_json(bars_json):
    return max(
            [(bar, bar['SeatsCount']) for bar in bars_json],
            key=operator.itemgetter(1)
            )[0]


def get_closest_bar_json(bars_json, local_longitude, local_latitude):
    return min(
            [(bar, calc_distance(
                                local_longitude,
                                local_latitude,
                                float(bar['Longitude_WGS84']),
                                float(bar['Latitude_WGS84'])))
             for bar in bars_json],
            key=operator.itemgetter(1)
            )[0]


def get_smallest_bar_json(bars_json):
    return min(
            [(bar, bar['SeatsCount']) for bar in bars_json],
            key=operator.itemgetter(1)
            )[0]


def load_data(filepath):
    if not os.path.exists(filepath):
        print('filepath does not exist')
        sys.exit()
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def prettify_json(json_data):
    return json.dumps(
                    json_data,
                    indent=4,
                    sort_keys=True,
                    ensure_ascii=False
                    )


def print_results(biggest_bar_json, smallest_bar_json, closest_bar_json):
    print('\nBiggest BAR:\n {}\n'.format(prettify_json(biggest_bar_json)))
    print('Smallest BAR:\n {}\n'.format(prettify_json(smallest_bar_json)))
    print('Closest BAR:\n {}\n'.format(prettify_json(closest_bar_json)))


def prompt_local_coordinates():
    try:
        return (
                float(input('Enter longitude:  ')),
                float(input('Enter latitude:  '))
                )
    except ValueError as e:
        print('You have enter digits')
        print('Example: Enter local longitude:  38.9')
        print('Example: Enter local latitude:  56.618')
        sys.exit()


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 bars.py "filepath/to/moscow_bars_json"\n')
        sys.exit()
    filepath_to_moscow_bars_json = sys.argv[1]
    bars_json = load_data(filepath_to_moscow_bars_json)
    local_longitude, local_latitude = prompt_local_coordinates()
    print_results(
            get_biggest_bar_json(bars_json),
            get_smallest_bar_json(bars_json),
            get_closest_bar_json(bars_json, local_longitude, local_latitude)
            )
