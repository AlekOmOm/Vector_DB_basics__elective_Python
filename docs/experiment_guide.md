# Vector Database Experimentation Guide

This guide provides some ideas for experimenting with your vector database implementation.

## 1. Add More Documents

Expand your sample data to include more information. You can add documents about:
- Advanced vector database concepts
- Real-world applications of embeddings
- Different similarity metrics
- Other vector database platforms

Example addition to `sample_data.py`:

```python
# Add these to the existing documents list
additional_documents = [
    "Euclidean distance measures the straight-line distance between two vectors in the vector space.",
    "Vector quantization is a technique used to compress vectors by mapping them to a finite set of representative vectors.",
    "Approximate nearest neighbor (ANN) algorithms sacrifice some accuracy for improved query performance in vector databases.",
    "Document retrieval in RAG (Retrieval-Augmented Generation) systems often uses vector databases to find relevant context for language models."
]

documents.extend(additional_documents)
```

After adding documents, regenerate your vector database by running `create_vectordb.py`.

## 2. Implement Metadata Filtering

Enhance your API to support filtering results based on metadata:

```python
# In api.py, modify the query function:
@app.route('/query', methods=['POST'])
def query():
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query_text = data['query']
    k = data.get('k', 2)
    
    # Get filter parameters if they exist
    metadata_filter = data.get('metadata_filter', None)
    
    # Search for similar documents with optional filter
    if metadata_filter:
        docs = vector_store.similarity_search(
            query_text, 
            k=k,
            filter=metadata_filter
        )
    else:
        docs = vector_store.similarity_search(query_text, k=k)
    
    # Format the results
    results = []
    for i, doc in enumerate(docs):
        results.append({
            'content': doc.page_content,
            'source': doc.metadata['source']
        })
    
    return jsonify({
        'query': query_text,
        'results': results,
        'filter_applied': metadata_filter is not None
    })
```

## 3. Try Different Distance Metrics

FAISS supports different distance metrics. Modify `create_vectordb.py` to experiment:

```python
# In create_vectordb.py
# For cosine similarity (default behavior)
vector_store = FAISS.from_documents(docs, embeddings)

# For inner product (dot product)
vector_store = FAISS.from_documents(
    docs, 
    embeddings,
    distance_strategy="INNER_PRODUCT"
)

# For Euclidean distance
vector_store = FAISS.from_documents(
    docs, 
    embeddings,
    distance_strategy="L2"
)
```

Compare the results of the same queries with different distance metrics.

## 4. Build a Simple Web Interface

Create a basic HTML frontend for your API. Create a file named `templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Vector Database Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .result { border:
