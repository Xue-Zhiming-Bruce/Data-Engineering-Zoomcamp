import dlt
from taxi_pipeline import taxi_pipeline

# Test basic import and structure
print("Testing taxi_pipeline import...")

# Create pipeline instance
pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb", 
    dataset_name="taxi_data"
)

# Test the source function
source = taxi_pipeline()
print(f"Source created: {source}")
print(f"Source name: {source.name}")

# Test the resource
resource = source.resources["taxi_trips"]
print(f"Resource: {resource}")
print(f"Resource name: {resource.name}")
print(f"Write disposition: {resource.write_disposition}")

print("✅ Pipeline structure test passed!")