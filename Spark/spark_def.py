"""
    This module includes a few functions(def) used to find out the top 10 videos with fastest growth of dislikes
    number between its first and second trending appearances. Raw data is handled by calling these def functions.

    Header has Attributes about "video_id", "trending_date", "category_id", "category", "publish_time", "views",
    "likes", "dislikes", "comment_count", "ratings_disabled", "video_error_or_removed" and "country".

"""


def Parse_Record(record):
    # video_id, trending_date, category, likes, dislikes, country = var[0], var[1], var[3], var[6], var[7], var[11]
    var = record.strip().split(",")
    trending_date = "%s%s.%s%s.%s%s" % (
        var[1][0], var[1][1], var[1][6], var[1][7],
        var[1][3], var[1][4])
    # To adjust the order of the month and day in the whole year. For sorting the date.
    return (var[0], var[11]), [[trending_date, var[3], var[6], var[7]]]

    # Ruturn & Generate a new tuple(key), the each element is a combination of multiple attributes.
    # For example: (('IP8k2xkhOdI', 'GB'), [['18.06.14', 'Music', 61998, 13781]])


def Merge_values(old_data, new_data):
    old_data.extend(new_data)
    return old_data

    # To merge records with the same key.
    # Return the result: e.g. (('AyiRO0_Ta7o', 'GB'), [['18.06.12', 'Sports', 6095, 248], ['18.06.13', 'Sports', 6191,
    # 251],['18.06.14', 'Sports', 6216, 252]])


def Affection_Calculation(key_value_pair):
    k, v = key_value_pair
    dislikes = int(v[1][3]) - int(v[0][3])
    likes = int(v[1][2]) - int(v[0][2])
    result = dislikes - likes
    return k[0], (result, v[0][1], k[1])

    # To calculate the value of growth rate
    # Return the result: ('DVWxQvlgRrM', (339, 'Entertainment', 'GB'))


def Get_Result(key_value_pair):
    # k expresses video_id, v[0]expresses growth number, v[1] means category, v[2] means country
    k, v = key_value_pair
    result = "%s,%s,%s,%s" % (k, v[0], v[1], v[2])
    return result
