from pyspark import SparkContext, SQLContext

if __name__ == '__main__':
    sc = SparkContext("local", "first app")
    sqlContext= SQLContext(sc)
    efile = sqlContext.read.parquet("hdfs://192.168.56.101:8020/hdata/people.parquet")
    efile.show()