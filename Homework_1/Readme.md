These are my solutions for questions in homework 1.

# Question 3

`SELECT COUNT(*)
FROM public.green_tripdata_2025_11
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
AND trip_distance <= 1`

# Question 4

`SELECT
	lpep_pickup_datetime::date AS pickup,
	SUM(trip_distance) AS total_distance
FROM public.green_tripdata_2025_11
WHERE trip_distance <= 100
GROUP BY pickup
ORDER BY SUM(trip_distance) DESC`

# Question 5

`SELECT a."Zone", SUM(b."total_amount") AS zone_amt
FROM taxi_zone_lookup a
JOIN green_tripdata_2025_11 b ON a."LocationID" = b."PULocationID"
WHERE lpep_pickup_datetime::date = '2025-11-18'
GROUP BY a."Zone"
ORDER BY zone_amt DESC`

# Question 6

`SELECT
	a."Zone",
	b."tip_amount",
	(
	SELECT taxi_zone_lookup."Zone"
	FROM taxi_zone_lookup
	WHERE taxi_zone_lookup."LocationID" = b."DOLocationID"
	) AS dropoff_location
FROM taxi_zone_lookup a
JOIN green_tripdata_2025_11 b ON a."LocationID" = b."PULocationID"
WHERE a."Zone" = 'East Harlem North'
ORDER BY b."tip_amount" DESC`
