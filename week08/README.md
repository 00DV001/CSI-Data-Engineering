# NYC Taxi Data Analysis with PySpark

This project focuses on ingesting NYC taxi trip data into a Data Lake, Blob Storage, or Databricks environment, processing it with PySpark, and executing analytical queries on the data.

## Problem Statement

![problem statement](/week08/screenshots/problemStatement.png)

## Dataset

This project utilizes the NYC Taxi Trip Record Data, focusing on the Yellow Taxi Trip Records for January 2020. The dataset contains detailed trip information, including pickup and drop-off times, locations, distances, and fares. It serves as the basis for data ingestion, processing, and analysis using PySpark in a Data Lake or Databricks environment.

- **Dataset URL**: [NYC Taxi Trip Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)
- **Direct Download Link**: [yellow_tripdata_2020-01.csv](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv)

## Prerequisites

-  Access to a Databricks environment or any equivalent big data platform.
-  Basic understanding of PySpark and SQL.
-  Availability of Blob Storage or Data Lake Storage to store the dataset.

## Setup

1. **Databricks Workspace**: Gain access to a Databricks workspace.
2. **Cluster Setup**: Configure a cluster with suitable resources to execute PySpark jobs.
3. **Library Installation**: Install all required libraries within the Databricks environment.

## Loading Data

1. **Download the Dataset**: Obtain the Yellow Taxi Trip dataset from the provided URL.
2. **Upload to DBFS**: Move the dataset to the Databricks File System (DBFS).

```python
#loading data from DBFS
file_location = "/FileStore/tables/yellow_tripdata_2020_01.csv"
file_type = "csv"

df = spark.read.format(file_type) \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .option("sep", ",") \
    .load(file_location)
```

## Processing and Flattening JSON Fields

If your dataset includes JSON fields, flatten them to simplify analysis and transformations.

```python
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# schema for the JSON column
json_schema = StructType([
    StructField("field1", StringType(), True),
    StructField("field2", DoubleType(), True)
    # more files if needed
])

# parse and flatten JSON fields
df = df.withColumn("flattened_data", from_json(col("json_column"), json_schema))
df = df.select("*", "flattened_data.*").drop("flattened_data", "json_column")
```

## Writing Flattened Data as External Parquet Table

After processing, save the DataFrame as an external Parquet table to enable fast and efficient querying.

```python
# write DataFrame to Parquet table
df.write.format("parquet").saveAsTable("yellow_taxi_data")
```

## Performing Queries

Below are key analytical queries applied to the dataset:

- **Query 1: Add a Revenue Column**

```python
df = df.withColumn("Revenue", col('Fare_amount') + col('Extra') + col('MTA_tax') +
                   col('Improvement_surcharge') + col('Tip_amount') +
                   col('Tolls_amount') + col('Total_amount'))
```

- **Query 2: Passenger Count by Pickup Area**

```python
passenger_count_by_area = df.groupBy("PULocationID").sum("passenger_count")
```

- ***Query 3: Average Total Fare by Vendor***

```python
average_fare_by_vendor = df.groupBy("VendorID").avg("Total_amount")
```

- **Query 4: Count of Payments by Payment Type**

```python
payment_mode_counts = df.groupBy("payment_type").count()
```

- **Query 5: Top 2 Vendors by Revenue on a Specific Date**

```python
windowSpec = Window.partitionBy("pickup_date").orderBy(col("Revenue").desc())

highest_gaining_vendors = df.withColumn("rank", rank().over(windowSpec)) \
                            .filter(col("rank") <= 2) \
                            .filter(col("pickup_date") == "2020-01-01")
```

- **Query 6: Route with Most Passengers**

```python
most_passengers_route = df.groupBy("PULocationID", "DOLocationID") \
                          .sum("passenger_count") \
                          .orderBy(col("sum(passenger_count)").desc()) \
                          .first()
```

- **Query 7: Top Pickup Locations in Last 10 Seconds**

```python
top_pickup_locations = df.filter(col("pickup_datetime") > current_timestamp() - expr("INTERVAL 10 seconds")) \
                         .groupBy("PULocationID") \
                         .sum("passenger_count") \
                         .orderBy(col("sum(passenger_count)").desc())
```

## Conclusion
This project showcases the end-to-end process of loading, transforming, and analyzing NYC taxi trip data using PySpark within a Databricks environment. By following the outlined steps, users can efficiently query the dataset and extract valuable insights through various analytical operations.
