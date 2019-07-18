import os

from pyspark import SparkContext

if __name__ == '__main__':
    logFile = os.path.join(os.getcwd(),"test.txt")
    sc = SparkContext("local", "first app")
    logData = sc.textFile(logFile).cache()
    numAs = logData.filter(lambda s: 'a' in s).count()
    numBs = logData.filter(lambda s: 'b' in s).count()
    print ("output=================",numAs,numBs)

