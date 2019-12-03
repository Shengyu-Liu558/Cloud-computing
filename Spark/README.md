### **Workload 2** **Spark** **Resources** (Work2)

This folder contains two implementations of files which are a def function file and main execution file and a execution shell file(.sh). Def function file is spark_def.py and main file is spark_execute.py.

1. run.sh is an shell implementation file, containing the execution phase. run.sh is a simple script using spark RDD. It takes two arguments: the input file and the output path. "

   

2. Environment setting:

   2.1 Add the environment variable PYSPARK python to have the python3.

   ```shell
   export PYSPARK_PYTHON =/usr/bin/python3
   ```

   2,2 If you want to output in you local place, you can use the coding below:

   ```shell
   spark-submit \
   
          --master local[2] \
   
          w2_TopTenWithFastestGrowthOfDislike.py \
   
          --input file:///home/hadoop/CloudAssignment/Work2/AllVideos_short.csv/ \
   
          --output file:///home/hadoop/CloudAssignment/Work2/
   
   ```

   Of course,if you do not configure path for output and input, the default output in HDFS and you need to input the absolute path. 

   

   2.3 Add the permissions for .sh file

   ```shell
   chmod 750 emr_submit.sh
   ```

   

   The input file is AllVideos_short.csv and confirm the structure of data, e.g.some attributes. Then the path of input should be correct.

    

   3.Execution of the (.sh) file:

   ```shell
   ./run.sh file:///../../../AllVideos_short.csv output
   ```

    

   4.you can check the output in HDFS:

   ```shell
   Hdfs dfs -cat output/part-*
   ```

   ```shell
   Hdfs dfs -ls output
   ```

   5.The final result is like: category  avg

   ```
    “ZGEoqPpJQLE”,98930,”Music”,”RU”
   ```

   

