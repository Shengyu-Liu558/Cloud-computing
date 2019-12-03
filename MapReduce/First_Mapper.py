#!/usr/bin/python3

"""
    This module includes a function(def) used to filter the whole data, then generate the new data which includes
    category,video_id and country.

    Header of '.csv' file has attributes about "video_id", "trending_date", "category_id", "category", "publish_time",
    "views", "likes", "dislikes", "comment_count", "ratings_disabled", "video_error_or_removed" and "country".

    This is a example about one line of result:People & Blogs,6ULbkqAuo48	GB. People & Blogs,6ULbkqAuo48 is the key.
    And GB is as value.

"""
import sys


def first_mapper():
    header = ["video_id"]
    for line in sys.stdin:
        line = line.strip()
        sets = line.split(",")
        if sets[0] == header[0]:
            continue
        category = sets[3].strip()
        o_id = sets[0].strip()
        country = sets[11].strip()
        marge = category + "," + o_id
        print("%s\t%s" % (marge, country))


if __name__ == "__main__":
    first_mapper()

