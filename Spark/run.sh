#!/bin/bash
#mkdir ~/data
#aws s3 cp s3://comp5349-2019/lab-data/a1_data/AllVideo_short.csv ~/data

spark-submit \
    --master local[3] \
    spark_execute.py \
    --input $1 \
    --output $2
    # --input file:///home/hadoop/CloudAssignment/Work2/AllVideos_short.csv/ \
    # --output file:///home/hadoop/CloudAssignment/Work2/

