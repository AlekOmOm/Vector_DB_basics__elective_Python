# tests/test_repository.py
import unittest
from unittest.mock import patch, MagicMock
import os
import tempfile

class TestVectorDBRepository(unittest.TestCase):
    
    def setUp(self):
        # Create temporary directory for test vector DB
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_faiss_index")
        
        # Set up mocks
        self.mock_embeddings = MagicMock()
        self.mock_documents = [
            MagicMock(page_content="Test document 1", metadata={"source": "doc_0"}),
            MagicMock(page_content="Test document 2", metadata={"source": "doc_1"})
        ]
    
    def tearDown(self):
        # Clean up temp directory
        self.temp_dir.cleanup()
    
    @patch('langchain_community.vectorstores.FAISS')
    def test_create_vector_store(self, mock_faiss):
        # Your test code here
        from src.vector_db.repository import VectorDBRepository
        
        # Arrange
        mock_faiss.from_documents.return_value = MagicMock()
        repository = VectorDBRepository()
        
        # Act
        result = repository.create_vector_store(self.mock_documents, self.mock_embeddings)
        
        # Assert
        mock_faiss.from_documents.assert_called_once_with(self.mock_documents, self.mock_embeddings)
        self.assertIsNotNone(result)
    
    @patch('langchain_community.vectorstores.FAISS')
    def test_save_vector_store(self, mock_faiss):
        # Test code for saving vector store

        from src.vector_db.repository import VectorDBRepository
        # Arrange




        
    @patch('langchain_community.vectorstores.FAISS')
    def test_load_vector_store(self, mock_faiss):
        # Test code for loading vector store
        pass
    
    @patch('langchain_community.vectorstores.FAISS')
    def test_singleton_pattern(self, mock_faiss):
        # Test that the repository follows singleton pattern
        from src.vector_db.repository import VectorDBRepository
        
        repo1 = VectorDBRepository.get_instance()
        repo2 = VectorDBRepository.get_instance()
        
        self.assertIs(repo1, repo2, "Repository should follow singleton pattern")
