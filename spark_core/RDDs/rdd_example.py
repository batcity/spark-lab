from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "spark-lab")

data = [1, 2, 3, 4, 5]
#distData is an RDD here
distData = sc.parallelize(data)

print(distData.collect())