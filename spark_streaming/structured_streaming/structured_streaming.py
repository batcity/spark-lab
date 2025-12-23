from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("StructuredStreamingExample").getOrCreate()

temperatures = spark.readStream.format("socket").option("host","localhost").option("port","9999").load()
temps_formatted = temperatures.select(col("value").cast("double").alias("temperature"))
temps_filtered_with_message = temps_formatted.select(col("temperature"),when(col("temperature") > 50,"warning - temperature is above 50 degrees!").alias("message"))

query = temps_filtered_with_message.writeStream.format("console").option("truncate", False).start()
query.awaitTermination()