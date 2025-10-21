from pyspark import SparkContext, StorageLevel
import time

sc = SparkContext("local","mem-check")

data = range(1000000)
datadist = sc.parallelize(range(10_000_000)).map(lambda x: x * x).filter(lambda x: x % 7 == 0)

print("first time calculation - but this is expensive because of the warm start problem")
start_time = time.time()
print(datadist.count())
end_time = time.time()
print(end_time - start_time)

datadist.persist(StorageLevel.MEMORY_ONLY)

print("second time calculation Note: includes persistence cost")
start_time = time.time()
print(datadist.count())
end_time = time.time()
print(end_time - start_time)

print("third time calculation uses persisted data - so it should be fast")
start_time = time.time()
print(datadist.count())
end_time = time.time()
print(end_time - start_time)

datadist.unpersist()

print("fourth time calculation unpersists data and recomputes the count - so it should be slow")
start_time = time.time()
print(datadist.count())
end_time = time.time()
print(end_time - start_time)

print("fifth time calculation recomputes the count - so it should be slow")
start_time = time.time()
print(datadist.count())
end_time = time.time()
print(end_time - start_time)

