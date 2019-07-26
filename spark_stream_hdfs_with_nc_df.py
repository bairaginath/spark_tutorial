#First have to start nc server as follow
# $ nc -lk 3333
# after that push following json
# {"name" : "bairagi" , "age" : 22 , "email" : "bairagi@gmail.com"}
# To run this as follow
# $SPARK_HOME/bin/spark-submit spark_stream_hdfs_with_nc_df.py


import json
from collections import namedtuple
from pyspark import SparkContext,Row,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

def convert_json(x):
    print(x)


# Create a local StreamingContext with two working threads and a batch interval of 10 seconds
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 10)


global sparkSessionSingletonInstance
# Create a DStream
lines = ssc.socketTextStream("localhost", 3333)

def getSparkSessionInstance(sparkConf):
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession\
            .builder\
            .config(conf=sparkConf)\
            .getOrCreate()
    return globals()['sparkSessionSingletonInstance']

def convert_row_rdd(x):
    #Convert to json to Object
    # obj=json.loads(x, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    # row=Row(name=obj.name,age=obj.age,email=obj.email)
    dict=json.loads(x)
    row=Row(name=dict.get("name"),age=dict.get("age"),email=dict.get("email"))
    return row


def process(time,rdd):
    print("========= %s =========" % str(time))
    if not rdd.isEmpty():
       rowRdd = rdd.map(convert_row_rdd)
       spark = getSparkSessionInstance(rdd.context.getConf())
       dataFrame = spark.createDataFrame(rowRdd)
       dataFrame.show()
       dataFrame.write.parquet("hdfs://0.0.0.0:9000/opt/people_spark_stream.parquet", mode="append")
       efile = spark.read.parquet("hdfs://0.0.0.0:9000/opt/people_spark_stream.parquet")
       efile.groupBy("name").count().show()




lines.foreachRDD(process)

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
