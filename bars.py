import json
from math import sqrt
import operator
import os
import sys


SECOND_ITEM = 1


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def prettify_json(jsn_data):
    return json.dumps(
                    jsn_data,
                    indent=4,
                    sort_keys=True,
                    ensure_ascii=False
                    )


def get_bars_with_seats_count(jsn_data):
    return [(bar, bar['SeatsCount']) for bar in jsn_data]


def get_biggest_bar(jsn_data):
    return max(
            get_bars_with_seats_count(jsn_data),
            key=operator.itemgetter(SECOND_ITEM)
            )[0]


def get_smallest_bar(jsn_data):
    return min(
            get_bars_with_seats_count(jsn_data),
            key=operator.itemgetter(SECOND_ITEM)
            )[0]


def calc_dist_to_bar(longitude_a, latitude_a, longitude_b, latitude_b):
    return sqrt(
                (pow((longitude_a - longitude_b), 2) +
                 pow((latitude_a - latitude_b), 2)),
                )


def get_bars_with_dists(jsn_data, longitude, latitude):
    return [(bar, calc_dist_to_bar(
                                    longitude,
                                    latitude,
                                    float(bar['Longitude_WGS84']),
                                    float(bar['Latitude_WGS84'])))
            for bar in jsn_data
            ]


def get_closest_bar(jsn_data, longitude, latitude):
    return min(
            get_bars_with_dists(jsn_data, longitude, latitude),
            key=operator.itemgetter(SECOND_ITEM)
            )[0]


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 bars.py "filepath"\n')
    filepath = sys.argv[1]
    jsn_data = load_data(filepath)
    if not jsn_data:
        print('filepath does not exist')
        sys.exit()
    try:
        longitude = float(input('Enter longitude:  '))
        latitude = float(input('Enter latitude:  '))
    except ValueError as e:
        print('You have to enter digits')
        print('Example: Enter longitude:  38.9')
        print('Example: Enter latitude:  56.618')
        sys.exit()
    biggest_bar = get_biggest_bar(jsn_data)
    smallest_bar = get_smallest_bar(jsn_data)
    closest_bar = get_closest_bar(jsn_data, longitude, latitude)
    print('\nThe biggest BAR is:\n {}\n'.format(prettify_json(biggest_bar)))
    print('The smallest BAR is:\n {}\n'.format(prettify_json(smallest_bar)))
    print('The closest BAR is:\n {}\n'.format(prettify_json(closest_bar)))
