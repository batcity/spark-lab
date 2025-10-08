import pyspark

sc = pyspark.SparkContext("local", "my-app")

words = ["mercedes", "volvo"]
dist_words = sc.parallelize(words)

# map is a transformation here
word_lengths = dist_words.map(lambda word: len(word))

print(word_lengths.collect())
# note reduce is an action
print("total world length is: ", word_lengths.reduce(lambda a, b: a + b))