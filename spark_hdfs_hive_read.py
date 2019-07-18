from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('hive-read').enableHiveSupport().getOrCreate()
    efile = spark.read.parquet("hdfs://0.0.0.0:9000/opt/people.parquet")
    efile.show()
