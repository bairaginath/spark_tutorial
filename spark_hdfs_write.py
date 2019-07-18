#To run this script with out yarn as follow
# $SPARK_HOME/bin//bin/spark-submit spark_hdfs_write.py


from pyspark import SparkContext, SQLContext
import time

if __name__ == '__main__':
    sc = SparkContext("local", "first app")
    sqlContext= SQLContext(sc)
    persion_dict={"name" : "james","favorite_color" : "black","favorite_numbers" : [7,11,123] }
    df=sqlContext.createDataFrame([persion_dict])
    df.show()
    while True:
        df.write.parquet("hdfs://0.0.0.0:9000/opt/people.parquet",mode="append")
        efile = sqlContext.read.parquet("hdfs://0.0.0.0:9000/opt/people.parquet")
        efile.show()
        time.sleep(1)
