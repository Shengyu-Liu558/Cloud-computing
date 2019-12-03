#!/usr/bin/python3

"""
    This module includes two functions(def) used to handle the data from the First Mapper, then generate the new data
    which is include (category,video_id)  and calculation of number of countries.

    This are examples about lines of result:(The number express the number of countries in same category and video_id)
                        Comedy,0FWDI-EUHkU	5.000000
                        Entertainment,HKDuDc3k_88	2.000000
                        News & Politics,at8CVrK9Gfo    2.000000
"""

import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split("\t", 1)


def first_reducer():
    merge = ""
    number_country = []
    number = 0

    data = read_map_output(sys.stdin)
    for var in data:
        global current_merge
        current_merge = var[0]
        country_name = var[1]
        if merge != current_merge:
            if merge != "":
                amount = len(number)
                print('%s\t%f' % (current_merge, amount))
            merge = current_merge
            number_country = []

        number_country.append(country_name)
        number = set(number_country)

    if merge != "":
        amount = len(number)
        print('%s\t%f' % (current_merge, amount))


if __name__ == "__main__":
    first_reducer()
