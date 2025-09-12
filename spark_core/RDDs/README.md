# Resilient Distributed Datasets (RDDs)

A **Resilient Distributed Dataset (RDD)** is the fundamental data structure in Apache Spark.  
It is an **immutable, fault-tolerant, distributed collection of elements** that can be processed in parallel across a cluster.  

---

## Key Characteristics

1. **Resilient**  
   RDDs are fault-tolerant. Spark tracks the transformations used to build an RDD in a **lineage graph (DAG)**, allowing lost or damaged data partitions to be recomputed automatically.  

2. **Distributed**  
   RDDs are divided into **partitions** across multiple nodes, enabling parallel processing. Each partition can be processed independently.  

3. **Dataset**  
   RDDs represent a collection of data records, which can come from **HDFS, local files, databases**, or by parallelizing existing collections in the driver program.  

4. **Immutable**  
   Once created, an RDD cannot be changed. Any transformation produces a **new RDD**.  

5. **Lazy Evaluation**  
   Transformations are **recorded but not executed immediately**. Computation occurs only when an **action** (like `collect()` or `count()`) is performed.  

---

## Example

Check out the implementation in [`rdd_example.py`](./rdd_example.py).

---

👉 RDDs give you **fine-grained control** over data and transformations, but for most modern workloads, **DataFrames** and **Datasets** are preferred since they provide higher-level APIs and better optimizations.
