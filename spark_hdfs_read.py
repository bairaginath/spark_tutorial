from pyspark import SparkContext, SQLContext

if __name__ == '__main__':
    sc = SparkContext("local", "first app")
    sqlContext= SQLContext(sc)
    efile = sqlContext.read.parquet("hdfs://0.0.0.0:9000/opt/people.parquet")
    row=efile.count()
    print "***************************number of records are *******************",row
    efile.show()
