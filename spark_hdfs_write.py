from pyspark import SparkContext, SQLContext

if __name__ == '__main__':
    sc = SparkContext("local", "first app")
    sqlContext= SQLContext(sc)
    persion_dict={"name" : "james","favorite_color" : "black","favorite_numbers" : [7,11,123] }
    df=sqlContext.createDataFrame([persion_dict])
    df.show()
    df.write.parquet("hdfs://192.168.56.101:8020/bbehera/people.parquet",mode="append")
    #df.write.save("hdfs://192.168.56.101:8020/bbehera/people.parquet",mode="append",format="parquet")
    efile = sqlContext.read.parquet("hdfs://192.168.56.101:8020/bbehera/people.parquet")
    efile.show()