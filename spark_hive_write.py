from pyspark import SparkContext, SQLContext
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName('abc').enableHiveSupport().getOrCreate()
    persion_dict={"name" : "manas","favorite_color" : "black","favorite_numbers" : [7,11,123] }
    df=spark.createDataFrame([persion_dict])
    df.show()
    df.write.parquet("hdfs://192.168.56.101:8020/bbehera/people.parquet",mode="append")
    #df.write.save("hdfs://192.168.56.101:8020/bbehera/people.parquet",mode="append",format="parquet")
    efile = spark.read.parquet("hdfs://192.168.56.101:8020/bbehera/people.parquet")
    efile.show()