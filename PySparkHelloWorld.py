import pyspark as spark

sparkContext = spark.SparkContext('local[*]')

bigList = range(10000)
rdd = sparkContext.parallelize(bigList, 2)
odds = rdd.filter(lambda n: n%2 != 0)

print(odds.count())

print(odds.take(5))
