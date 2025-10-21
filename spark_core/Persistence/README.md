# Spark Persistence Example

## 🧠 Persistence in Apache Spark

The **Persistence API** in Spark allows you to **cache or persist RDDs** (and DataFrames) in **memory**, **disk**, or a combination of both.  

This helps Spark **reuse previously computed data** instead of recomputing it every time an action is triggered — which is especially valuable for **iterative or expensive computations** (e.g., machine learning algorithms, graph processing, etc.).

## 💾 Why Persistence Matters
- Avoids recomputation of the same RDD across multiple actions.  
- Improves performance for iterative workloads.  
- Allows trade-offs between **speed** (memory) and **resource usage** (disk).

## ⚙️ Common Storage Levels

| Level | Description |
|-------|-------------|
| `MEMORY_ONLY` | Store RDD as deserialized Java/Python objects in memory. |
| `MEMORY_AND_DISK` | Store in memory if possible; spill to disk if not. |
| `DISK_ONLY` | Persist only to disk (used when memory is limited). |
| `MEMORY_ONLY_SER` | Store in memory as serialized data (less space, more CPU). |

## 🧩 Example (Python)

```python
from pyspark import SparkContext, StorageLevel

sc = SparkContext("local", "PersistenceExample")

data = sc.parallelize(range(1000000))
data.persist(StorageLevel.MEMORY_ONLY)

print(data.count())  # Cached after first action
print(data.count())  # Reads from memory
````

## 📊 In this folder

This example demonstrates:

* Timing the cost of recomputation vs cached access
* Using `persist()` and `unpersist()`
* Observing Spark’s caching behavior through repeated actions

## 📘 References

* [Spark RDD Persistence Documentation](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence)
* [Spark StorageLevel API](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.html)

## ✅ TL;DR

> **Caching / Persistence** in Spark trades **memory** for **speed**,
> letting you reuse expensive computations efficiently.