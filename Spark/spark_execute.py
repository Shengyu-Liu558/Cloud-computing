"""
    This module include a execution functions(def) used to handle the raw data step by step , then generate the final
    files which includes video_id, growth number, category and country.

    There is the final result which are saved in file:
                QwZT7T-TXT0,189608,Entertainment,US
                QwZT7T-TXT0,189605,Entertainment,GB
                ...
                84LBjXaeKk4,93961,Entertainment,RU
"""


from pyspark import SparkContext
from spark_def import *
import argparse


def spark_exc():
    sc = SparkContext(appName="Controversial Trending Videos Identification")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path", default="AllVideos_short.csv")
    parser.add_argument("--output", help="the output path", default="output")
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    initial_data = sc.textFile(input_path)  # To read the raw file(.csv)

    header = "video_id"
    first_filter = initial_data.filter(lambda x: x[0] != header[0])
    # 1: To delete the first line in raw data(meanings headers).

    second_filter = first_filter.map(Parse_Record)
    # 2: To map the function generated in the previous step to another RDD

    third_filter = second_filter.reduceByKey(Merge_values)
    # 3: To merge records with the same key

    fourth_filter = third_filter.filter(lambda x: len(x[1]) >= 2)
    # 4: To filter the number of values is more than 2.

    fifth_filter = fourth_filter.map(Affection_Calculation)
    # 5: To generate the another RDD that includes video_id,growth_number,category and country.

    sixth_filter = fifth_filter.sortBy(keyfunc=lambda x: x[1][0], ascending=False).take(10)
    # 6: To sort data and take the top 10.

    result_top_ten = sc.parallelize(sixth_filter)
    # 7: To generate the another RDD.

    result_top_ten.map(Get_Result).saveAsTextFile(output_path)
    # 8: Save the result to output.


if __name__ == "__main__":
    spark_exc()
