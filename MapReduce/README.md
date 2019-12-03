## Workload 1 Map Reduce Resources (Work1)

This folder contains two implementations of job and an execution shell file(.sh). First job includes the First_Mapper.py and First_Reducer.py. Second job has two python files which are Second_Mapper.py and Second_Reducer.py.

1.run.sh is a shell implementation file, containing the two maps and two reduces phase. run.sh is a simple script provided using streaming API. It takes two arguments: the input file and the output path. Since two jobs need to be running, this process produces an output as input to second job. Below is an example:(when shell file is running in AWS (emr), the input needs to write an absolute path) 

```shell
./run.sh AllVideos_short.csv final_output
```

2. The input and output already have written in run.sh. However, the path needs to be change when the mapper and reducer file are not with run.sh in a folder, because shell file needs to find the mapper and reducer files. 

3. Environment setting: 

   a)         Python 3 environment

   b)         To change the path of the Hadoop jar that you can find it. 

   ```shell
   hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-2.jar \
   ```

   c)         Add the permissions for (.sh) file (chmod 750 run.sh). you need to execute the shell file. 

   

4. The input file is AllVideos_short.csv and confirm the structure of data such as some attributes. Then the path of input should be correct. 

5. The output is stored by default in HDFS. So, the output can be check in HDFS. The code is:

   ```
   hdfs dfs -cat output/part - *
   ```

   ```
   hdfs dfs -ls output
   ```

6. The final result is like: category   avg

```
                Autos & Vehicles     1.02
                Comedy   1.21
                ...
                Trailers     1.00
                Travel & Events        1.09
```

