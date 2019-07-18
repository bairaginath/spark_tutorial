from operator import add

from pyspark import SparkContext
sc = SparkContext("local", "Map app")
words = sc.parallelize (
   ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
    "spark",
   "pyspark and spark"]
)

counter_dict={}
def f(x):
    if counter_dict.get(x) == None:
        counter_dict[x] = 1
    else:
        counter_dict[x] = counter_dict.get(x) + 1

words_map = words.map(f)
mapping = words_map.collect()
print ("Key value pair -> {}".format(mapping))
print ("============")
print (counter_dict)

nums = sc.parallelize([1, 2, 3, 4, 5])
adding = nums.reduce(add)
print(adding)

# num = sc.accumulator(10)


num = 10

def f(x):
   global num
   print (num)
   num+=x
rdd = sc.parallelize([20,30,40,50])
rdd.foreach(f)
final = num
print  (final)
