# Question 2

```
SELECT COUNT(*) as record_count
FROM `dido-486313.dbt_prod.fct_monthly_zone_revenue`;
```

# Question 3

```
SELECT COUNT(*) as record_count
FROM `dido-486313.dbt_prod.fct_monthly_zone_revenue`;
```

# Question 4

```
SELECT 
  z.zone,
  SUM(f.revenue_monthly_total_amount) as total_revenue
FROM `dido-486313.dbt_prod.fct_monthly_zone_revenue` f
JOIN `dido-486313.dbt_prod.dim_zones` z 
  ON f.zone_id = z.locationid
WHERE f.service_type = 'Green'
  AND f.revenue_month BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY z.zone
ORDER BY total_revenue DESC
LIMIT 1;
```

# Question 5

```
SELECT COUNT(*) as total_trips
FROM `dido-486313.dbt_prod.fct_trips` 
WHERE service_type = 'Green'
  AND pickup_datetime >= '2019-10-01'
  AND pickup_datetime < '2019-11-01';
```

# Question 6

```
SELECT COUNT(*) as record_count
FROM `dido-486313.dbt_prod.stg_fhv_tripdata`;
```
