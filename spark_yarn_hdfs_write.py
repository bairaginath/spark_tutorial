#To run this script with  yarn as follow
# $SPARK_HOME/bin/spark-submit --master yarn --deploy-mode cluster  spark_yarn_hdfs_write.py


from pyspark import SparkContext, SQLContext
import time
from pyspark import SparkConf

if __name__ == '__main__':
    conf = SparkConf()
    conf.setMaster('yarn')
    conf.setAppName('spark-yarn')
    sc = SparkContext(conf=conf)
    sqlContext= SQLContext(sc)
    persion_dict={"name" : "james","favorite_color" : "black","favorite_numbers" : [7,11,123] }
    df=sqlContext.createDataFrame([persion_dict])
    df.show()
    while True:
        df.write.parquet("hdfs://0.0.0.0:9000/opt/people_yarn.parquet",mode="append")
        efile = sqlContext.read.parquet("hdfs://0.0.0.0:9000/opt/people_yarn.parquet")
        efile.show()
        time.sleep(1)
