#!/usr/bin/python3

"""

    This module includes a function(def) used to filter the data form the First Reducer, then generate the new data
    which includes category, the number of countries.

    This are examples about lines of result:
        Autos & Vehicles	2.000000
        Comedy	3.000000
        Comedy	7.000000
        Entertainment	2.000000


"""

import sys


def second_mapper():
    for line in sys.stdin:
        line = line.strip()
        sets = line.split("\t")
        cate = sets[0].split(",")
        category = cate[0]
        number_country = sets[1].strip()
        print("%s\t%s" % (category, number_country))


if __name__ == "__main__":
    second_mapper()
