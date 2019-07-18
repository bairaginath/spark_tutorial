from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('abc').enableHiveSupport().getOrCreate()
    efile = spark.read.parquet("hdfs://192.168.56.101:8020/hdata/people.parquet")
    sql(efile).show()