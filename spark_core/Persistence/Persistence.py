from pyspark import SparkConf, SparkContext, StorageLevel
import time

# --- Configure Spark ---
conf = (
    SparkConf()
    .setAppName("persist-demo")
    .setMaster("local[*]")
    .set("spark.executor.memory", "2g")
    .set("spark.driver.memory", "2g")
)

sc = SparkContext(conf=conf)

# --- Generate a large dataset ---
print("generating large dataset...")
sample_data = [f"item_{i}" for i in range(10_000_000)]
rdd = sc.parallelize(sample_data, numSlices=8)

# --- Expensive transformation ---
def expensive_map(x):
    return (x, x.upper())

rdd_transformed = rdd.map(expensive_map)

# --- Without persistence ---
print("\n=== Without persistence ===")
# 1️⃣ Count
start = time.time()
rdd_transformed.count()
print("Action 1 (count) took:", time.time() - start)

# 2️⃣ Take first 5 elements
start = time.time()
sample = rdd_transformed.take(5)
print("Action 2 (take 5) took:", time.time() - start)
print("Sample:", sample)

# 3️⃣ Filter and count
start = time.time()
filtered_count = rdd_transformed.filter(lambda x: "999" in x[0]).count()
print("Action 3 (filter count) took:", time.time() - start)
print("Filtered count:", filtered_count)

# --- Persist to memory and disk ---
rdd_transformed.persist(StorageLevel.MEMORY_ONLY)
print("\nNote: This is Spark persistence for performance. "
      "It is NOT permanent storage like writing Avro/Parquet files.\n")

# --- With persistence: same three actions ---
print("=== With persistence (three actions) ===")

# 1️⃣ Count (first action triggers computation + caching)
start = time.time()
rdd_transformed.count()
print("Action 1 (count) took:", time.time() - start)
print(
    "Note: The first action after persist is slower because Spark uses lazy evaluation. "
    "At this point, the RDD has not been computed yet, so Spark must compute all partitions "
    "and store them in the cache (memory and/or disk). Subsequent actions are faster because "
    "they can read the cached data without recomputing the transformations."
)

# 2️⃣ Take first 5 elements (reads from cache)
start = time.time()
sample = rdd_transformed.take(5)
print("Action 2 (take 5) took:", time.time() - start)
print("Sample:", sample)

# 3️⃣ Filter and count (reads from cache)
start = time.time()
filtered_count = rdd_transformed.filter(lambda x: "999" in x[0]).count()
print("Action 3 (filter count) took:", time.time() - start)
print("Filtered count:", filtered_count)

# --- Cleanup ---
rdd_transformed.unpersist()
sc.stop()