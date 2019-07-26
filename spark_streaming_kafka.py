#To download and start kafka server
#wget http://apache.claz.org/kafka/2.3.0/kafka_2.11-2.3.0.tgz
#tar xvfz kafka/2.3.0/kafka_2.11-2.3.0.tgz
#export KAFKA_HOME="/home/bairagi/spark/kafka_2.11-2.3.0/"
# cd $KAFKA_HOME/bin
# ./zookeeper-server-start.sh ../config/zookeeper.properties
# ./kafka-server-start.sh ../config/server.properties
#create topic as below
#./kafka-console-producer.sh --broker-list localhost:9092 --topic spark-kafka

# producer end
# ./kafka-console-producer.sh --broker-list localhost:9092 --topic spark-kafka

#consumer end
# ./kafka-console-consumer.sh --bootstrap-server 0.0.0.0:9092 --topic spark-kafka

#To run this script as follow
#$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.2 ../../spark_tutorial/spark_streaming_kafka.py localhost:9092 spark-kafka



import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    #sc = SparkContext(appName= "PythonStreamingDirectKafkaWordCount" )
    sc = SparkContext("local[2]", "KafkaWordCount")
    ssc = StreamingContext(sc, 10)
    brokers, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})
    #kvs = KafkaUtils.createStream(ssc,brokers,"raw-event-streaming-consumer",{topic:1}) 
    lines = kvs.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a+b)    
    print("************************************************************************************************")
    print(lines)
    words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
    print(words)
    counts.pprint()
    print("================================================================================================")
    ssc.start()
    ssc.awaitTermination()
