from pyspark import SparkContext, SQLContext
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('hive-write').enableHiveSupport().getOrCreate()
    persion_dict={"name" : "manas","favorite_color" : "black","favorite_numbers" : [7,11,123] }
    df=spark.createDataFrame([persion_dict])
    df.show()
    df.write.parquet("hdfs://0.0.0.0:9000/opt/people.parquet",mode="append")
    efile = spark.read.parquet("hdfs://0.0.0.0:9000/opt/people.parquet")
    efile.groupBy("name").count().show()
