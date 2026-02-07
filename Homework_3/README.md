# BigQuery Code for Homework

```
-- Step 1: Create the dataset
CREATE SCHEMA IF NOT EXISTS `ny_taxi_2024`;

-- Step 2: Load data from GCS into a Native BigQuery Table
LOAD DATA OVERWRITE `ny_taxi_2024.yellow_tripdata_2024`
FROM FILES (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-by-dido/yellow_tripdata_2024-*.parquet']
);

CREATE OR REPLACE EXTERNAL TABLE `ny_taxi_2024.external_yellow_tripdata_2024`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-by-dido/yellow_tripdata_2024-*.parquet']
);

-- Question 1
SELECT COUNT(*)
FROM ny_taxi_2024.yellow_tripdata_2024;

-- Question 2
SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi_2024.yellow_tripdata_2024`;

SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi_2024.external_yellow_tripdata_2024`;

-- Question 3
SELECT COUNT(DISTINCT PULocationID), COUNT(DISTINCT DOLocationID)
FROM `ny_taxi_2024.yellow_tripdata_2024`;

-- Question 4
SELECT COUNT(fare_amount)
FROM `ny_taxi_2024.yellow_tripdata_2024`
WHERE fare_amount = 0;

-- Question 5
CREATE OR REPLACE TABLE `ny_taxi_2024.yellow_tripdata_2024_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * FROM `ny_taxi_2024.yellow_tripdata_2024`;

-- Question 6
SELECT DISTINCT VendorID
FROM `ny_taxi_2024.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT VendorID
FROM `ny_taxi_2024.yellow_tripdata_2024_optimized`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

-- Question 9
SELECT count(*) FROM `ny_taxi_2024.yellow_tripdata_2024`;


```
