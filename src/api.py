



#      "code": "# api.py\n\nfrom flask import Flask, request, jsonify\nimport os\nfrom dotenv import load_dotenv\nfrom langchain.embeddings.openai import OpenAIEmbeddings\nfrom langchain.vectorstores import FAISS\n\n# Load environment variables\nload_dotenv()\n\napp = Flask(__name__)\n\n# Initialize the OpenAI embeddings\nembeddings = OpenAIEmbeddings()\n\n# Load the vector store\nvector_store = FAISS.load_local(\"faiss_index\", embeddings)\n\n@app.route('/query', methods=['POST'])\ndef query():\n    data = request.json\n    if not data or 'query' not in data:\n        return jsonify({'error': 'No query provided'}), 400\n    \n    query_text = data['query']\n    k = data.get('k', 2)  # Number of results to return, default is 2\n    \n    # Search for similar documents\n    docs = vector_store.similarity_search(query_text, k=k)\n    \n    # Format the results\n    results = []\n    for i, doc in enumerate(docs):\n        results.append({\n            'content': doc.page_content,\n            'source': doc.metadata['source']\n        })\n    \n    return jsonify({\n        'query': query_text,\n        'results': results\n    })\n\nif __name__ == '__main__':\n    app.run(debug=True)"

from flask import Flask, request, jsonify
import os
from env.secrets_manager import SecretsManager
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


# Load environment variables

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGSMITH_PROJECT'] = "Python RAG undervisning"

os.environ['LANGCHAIN_API_KEY'] = SecretsManager.get_secret("Langchain_API_Key", "credential", "API_Keys")
os.environ['OPENAI_API_KEY'] = SecretsManager.get_secret("OpenAI_API_Key", "credential", "API_Keys")

## =============================================================================
## =============================================================================
## == Flask App - API 

app = Flask(__name__)

