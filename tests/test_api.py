# tests/test_api.py
import unittest
import json
from unittest.mock import patch, MagicMock
from src.api import app

class TestVectorDBAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Setup mock service
        self.mock_service = MagicMock()
        self.mock_docs = [
            {'content': 'Result 1', 'source': 'doc_0'},
            {'content': 'Result 2', 'source': 'doc_1'}
        ]
    
    @patch('src.vector_db.service.VectorDBService')
    def test_query_endpoint(self, mock_service_class):
        # Arrange
        mock_service_instance = MagicMock()
        mock_service_class.get_instance.return_value = mock_service_instance
        mock_service_instance.query_and_format.return_value = self.mock_docs
        
        # Act
        response = self.app.post('/query', 
                               data=json.dumps({'query': 'test query', 'k': 2}),
                               content_type='application/json')
        
        # Assert
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['results'], self.mock_docs)
        mock_service_instance.query_and_format.assert_called_once_with('test query', 2)
    
    @patch('src.vector_db.service.VectorDBService')
    def test_query_endpoint_validation(self, mock_service_class):
        # Test validation for missing query
        response = self.app.post('/query', 
                               data=json.dumps({'k': 2}),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
