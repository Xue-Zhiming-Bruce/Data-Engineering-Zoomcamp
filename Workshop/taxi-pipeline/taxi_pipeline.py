import dlt
from dlt.sources.helpers.rest_client import paginate
from dlt.sources.helpers.rest_client.auth import BearerTokenAuth
from dlt.sources.helpers.rest_client.paginators import BasePaginator


class TaxiPaginator(BasePaginator):
    def __init__(self):
        super().__init__()
        self.current_page = 0
    
    def update_state(self, response, data) -> None:
        """Update pagination state from response"""
        # Stop if we get an empty page
        if not data or len(data) == 0:
            self._has_next_page = False
            return
            
        # Increment page for next request
        self.current_page += 1
        
    def update_request(self, request) -> None:
        """Update request with pagination parameters"""
        if request.params is None:
            request.params = {}
        request.params["page"] = self.current_page


@dlt.source(name="taxi_data")
def taxi_pipeline():
    """
    NYC taxi data pipeline using REST API with pagination.
    Fetches paginated JSON data (1000 records per page) from the API.
    """
    
    @dlt.resource(name="taxi_trips", write_disposition="append")
    def taxi_trips():
        # Configure the API client
        api_url = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
        
        # Use the custom paginator
        paginator = TaxiPaginator()
        
        # Paginate through the API
        for page_data in paginate(api_url, paginator=paginator):
            # Yield each record from the page
            if page_data:
                for record in page_data:
                    yield record
            else:
                # Stop if we get an empty page
                break
    
    return taxi_trips


if __name__ == "__main__":
    # Test the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="taxi_data"
    )
    
    # Run the pipeline
    load_info = pipeline.run(taxi_pipeline())
    print(load_info)