# Question 1

```
SELECT 
    MIN(trip_pickup_date_time) as start_date,
    MAX(trip_pickup_date_time) as end_date
FROM taxi_trips
```

# Question 2

```
SELECT 
    payment_type,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
FROM taxi_trips
GROUP BY payment_type
ORDER BY percentage DESC
```

# Question 3

```
SELECT SUM(tip_amt) as total_tip
FROM taxi_trips
```
