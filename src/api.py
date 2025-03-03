#      "code": "# api.py\n\nfrom flask import Flask, request, jsonify\nimport os\nfrom dotenv import load_dotenv\nfrom langchain.embeddings.openai import OpenAIEmbeddings\nfrom langchain.vectorstores import FAISS\n\n# Load environment variables\nload_dotenv()\n\n
# app = Flask(__name__)\n\n# Initialize the OpenAI embeddings\nembeddings = OpenAIEmbeddings()\n\n
# # Load the vector store\nvector_store = FAISS.load_local(\"faiss_index\", embeddings)\n\n
# @app.route('/query', methods=['POST'])\ndef query():\n    data = request.json\n    if not data or 'query' not in data:\n        return jsonify({'error': 'No query provided'}), 400\n    \n    query_text = data['query']\n    k = data.get('k', 2)  # Number of results to return, default is 2\n    \n    # Search for similar documents\n    docs = vector_store.similarity_search(query_text, k=k)\n    \n    # Format the results\n    results = []\n    for i, doc in enumerate(docs):\n        results.append({\n            'content': doc.page_content,\n            'source': doc.metadata['source']\n        })\n    \n    return jsonify({\n        'query': query_text,\n        'results': results\n    })\n\nif __name__ == '__main__':\n    app.run(debug=True)"

import os
import sys
# Add project root to sys.path to resolve the "env" package correctly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify


from vector_db.create_vectordb import VectorDB
from vector_db.query_vectordb import Query_DB


## =============================================================================
## =============================================================================
## == Flask App - API 

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
      data = request.json
      if not data or 'query' not in data:
         return jsonify({'error': 'No query provided'}), 400
      
      query_text = data['query']
      k = data.get('k', 2)  # Number of results to return, default is 2

      # Search for similar documents
      Query_DB.query_vector_db(query_text, k=k)
      