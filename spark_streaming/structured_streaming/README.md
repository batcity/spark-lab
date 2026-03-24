# Spark Structured Streaming

Spark structured streaming is the current standard for stream processing within Spark. In this library, spark treats all incoming streaming data as if it were an unbounded table where data is being continuously appended. This allows developers to write processing pipelines using the same APIs as for batch (bounded) data. However, the data must conform to a defined schema, as Structured Streaming operates on structured datasets.

You can stream unstructured data, but you must apply a structuring step before using standard Structured Streaming operations.