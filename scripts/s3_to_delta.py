from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("S3-Delta-Process").getOrCreate()

# Read raw JSON from S3
df = spark.read.json("s3://<YOUR_BUCKET>/streaming/raw/")

# Convert and write into Delta Lake format (processed zone)
df.write.format("delta") \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .save("s3://<YOUR_BUCKET>/streaming/processed/delta_ecommerce/")
