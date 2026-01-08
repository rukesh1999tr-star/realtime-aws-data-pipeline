# Real-Time AWS Data Engineering Project
## E-Commerce Clickstream Pipeline

### 🔹 Pipeline Flow
Python Event Generator → AWS MSK (Kafka) → Spark Streaming (EMR) → S3 (Raw Data Lake) → Delta Lake (Processed) → Snowflake → Dashboard

### 🔹 Tech Used
- Python, PySpark, Kafka, AWS MSK, EMR, S3, Delta Lake, IAM, CloudWatch
- BI: Power BI / Tableau
- Data Validation: Great Expectations

### 🔹 Features
- Real-time streaming ingestion
- Spark fault tolerance using S3 checkpoints
- Delta Lake schema evolution
- Data lake layered design (raw → processed)
- IAM secured and monitored pipeline
