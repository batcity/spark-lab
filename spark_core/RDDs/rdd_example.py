from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "spark-lab")

data = ["apple", "orange", "avocado"]
#distData is an RDD here
distData = sc.parallelize(data)

print(distData.collect())