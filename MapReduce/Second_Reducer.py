#!/usr/bin/python3

"""

    This module includes two functions(def) used to handle the data from the Second Mapper, then generate the final
    files which includes category and the average value.

    There is the final result which are saved in file:
                Autos & Vehicles	1.02
                Comedy	1.21
                ...
                Trailers	1.00
                Travel & Events	1.09

"""

import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")


def second_reducer():
    category = None
    count = 0.0
    frequency = 0.0
    data = read_map_output(sys.stdin)
    for var in data:
        current_category = var[0]
        country_num = var[1]

        if category != current_category:
            if category is not None:
                result = (count / frequency)
                print('%s\t%.2f' % (category, result))
            category = current_category
            count = 0.0
            frequency = 0.0

        frequency += 1.0
        count += float(country_num)

    if category is not None:
        result = (count / frequency)
        print('%s\t%.2f' % (category, result))


if __name__ == "__main__":
    second_reducer()
