# Testing the Vector Database API with Postman

This guide will help you test the vector database API using Postman.

## Prerequisites
- Ensure you have completed steps 1-5 of the vector database exercise
- Make sure the API server is running with `python api.py`
- Postman is installed on your system

## Import the Collection
1. Open Postman
2. Click "Import" in the top left
3. Select the `vector_db_postman_collection.json` file from this repository
4. Click "Import"

## Test the API
1. In the Postman sidebar, you'll see the "Vector DB API" collection
2. Expand it to see the pre-configured requests
3. Select "Query Vector DB" to start with
4. Click the "Send" button to execute the request
5. You should see a JSON response with results matching your query

## Experiment with Different Queries
The collection includes several pre-configured queries:
- Basic vector database functionality
- Cosine similarity information
- Vector database use cases
- Traditional vs. vector databases

Feel free to modify the query text and the `k` value (number of results) to experiment.

## Troubleshooting
- If you get a connection error, make sure the API server is running on port 5000
- If you get a 500 error, check the console output of the API server for details
- If the results seem incorrect, ensure you've properly created and populated the vector database in Step 3

## Next Steps
After successfully testing with Postman, you can mark Step 6 as completed in your to-do.json file and move on to Step 7: Experiment and Learn.
