# tests/test_service.py
import unittest
from unittest.mock import patch, MagicMock

class TestVectorDBService(unittest.TestCase):
    
    def setUp(self):
        # Setup mock repository
        self.mock_repository = MagicMock()
        self.mock_vector_store = MagicMock()
        self.mock_repository.get_vector_store.return_value = self.mock_vector_store
        
        # Mock query results
        self.mock_docs = [
            MagicMock(page_content="Result 1", metadata={"source": "doc_0"}),
            MagicMock(page_content="Result 2", metadata={"source": "doc_1"})
        ]
        self.mock_vector_store.similarity_search.return_value = self.mock_docs
    
    @patch('src.vector_db.repository.VectorDBRepository')
    def test_query_vector_db(self, mock_repo_class):
        # Arrange
        from src.vector_db.service import VectorDBService
        mock_repo_class.get_instance.return_value = self.mock_repository
        
        service = VectorDBService()
        query_text = "test query"
        k = 2
        
        # Act
        results = service.query_vector_db(query_text, k)
        
        # Assert
        self.mock_vector_store.similarity_search.assert_called_once_with(query_text, k=k)
        self.assertEqual(results, self.mock_docs)
    
    @patch('src.vector_db.repository.VectorDBRepository')
    def test_format_results(self, mock_repo_class):
        # Test formatting of results
        from src.vector_db.service import VectorDBService
        service = VectorDBService()
        
        formatted = service.format_results(self.mock_docs)
        
        expected = [
            {'content': 'Result 1', 'source': 'doc_0'},
            {'content': 'Result 2', 'source': 'doc_1'}
        ]
        
        self.assertEqual(formatted, expected)
