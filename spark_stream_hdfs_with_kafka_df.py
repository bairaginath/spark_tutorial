#To download and start kafka server
#wget http://apache.claz.org/kafka/2.3.0/kafka_2.11-2.3.0.tgz
#tar xvfz kafka/2.3.0/kafka_2.11-2.3.0.tgz
#export KAFKA_HOME="/home/bairagi/spark/kafka_2.11-2.3.0/"
# cd $KAFKA_HOME/bin
# ./zookeeper-server-start.sh ../config/zookeeper.properties
# ./kafka-server-start.sh ../config/server.properties

#create topic as below
# ./kafka-console-consumer.sh --bootstrap-server 0.0.0.0:9092 --topic spark-kafka

# producer end
# ./kafka-console-producer.sh --broker-list localhost:9092 --topic spark-kafka

#consumer end
# ./kafka-console-consumer.sh --bootstrap-server 0.0.0.0:9092 --topic spark-kafka

#To run this script as follow
#$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.2  ../../spark_tutorial/spark_stream_hdfs_with_kafka_df.py localhost:9092 spark-kafka

#After that push data on producer topic as below
#{"name" : "bairagi1" , "age" : 22 , "email" : "bairagi@gmail.com"}


##To DO
# Exception handling have to do


import json
from collections import namedtuple
import sys
from pyspark import SparkContext,Row,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession

global sparkSessionSingletonInstance

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
       dataFrame.write.parquet("hdfs://0.0.0.0:9000/opt/people_spark_stream_kafka.parquet", mode="append")
       efile = spark.read.parquet("hdfs://0.0.0.0:9000/opt/people_spark_stream_kafka.parquet")
       efile.groupBy("name").count().show()



if __name__ == "__main__":
    #sc = SparkContext(appName= "PythonStreamingDirectKafkaWordCount" )
    sc = SparkContext("local[2]", "KafkaWordCount")
    ssc = StreamingContext(sc, 10)
    brokers, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})
    #kvs = KafkaUtils.createStream(ssc,brokers,"raw-event-streaming-consumer",{topic:1}) 
    lines = kvs.map(lambda x: x[1])
    lines.foreachRDD(process)
    ssc.start()
    ssc.awaitTermination()
