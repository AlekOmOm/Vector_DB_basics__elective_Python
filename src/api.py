# src/api.py
from flask import Flask, request, jsonify
from src.vector_db.service import VectorDBService

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query_text = data['query']
    k = data.get('k', 2)
    
    try:
        service = VectorDBService.get_instance()
        results = service.query_and_format(query_text, k)
        
        return jsonify({
            'query': query_text,
            'results': results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
