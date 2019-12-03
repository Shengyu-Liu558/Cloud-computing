#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./run.sh [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-2.jar \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='First job to get the new data by filtering.' \
-file First_Mapper.py \
-mapper First_Mapper.py \
-file First_Reducer.py \
-reducer First_Reducer.py \
-input $1 \
-output output1 \


hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-2.jar \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Second job to get the final result.' \
-file Second_Mapper.py \
-mapper Second_Mapper.py \
-file Second_Reducer.py \
-reducer Second_Reducer.py \
-input output1 \
-output $2
