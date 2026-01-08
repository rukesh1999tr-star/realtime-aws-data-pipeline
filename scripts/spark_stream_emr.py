from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

spark = SparkSession.builder.appName("RealTime-MSK-Spark").getOrCreate()

# Define schema of incoming Kafka JSON
schema = StructType([
    StructField("user_id", IntegerType()),
    StructField("event", StringType()),
    StructField("product_id", IntegerType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", LongType())
])

# Read stream from AWS MSK Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "<MSK_BROKER_ENDPOINT>") \
    .option("subscribe", "ecommerce-events") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse JSON events
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write raw stream to S3 for data lake storage
query = parsed_df.writeStream \
    .format("json") \
    .option("path", "s3://<YOUR_BUCKET>/streaming/raw/") \
    .option("checkpointLocation", "s3://<YOUR_BUCKET>/streaming/checkpoint/") \
    .outputMode("append") \
    .start()

query.awaitTermination()
