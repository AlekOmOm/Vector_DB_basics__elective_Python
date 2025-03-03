# src/vector_db/service.py
from src.vector_db.repository import VectorDBRepository

class VectorDBService:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.repository = VectorDBRepository.get_instance()
    
    def query_vector_db(self, query_text, k=2):
        """Query the vector database"""
        vector_store = self.repository.get_vector_store()
        if not vector_store:
            raise ValueError("Vector store not initialized")
            
        return vector_store.similarity_search(query_text, k=k)
    
    def format_results(self, docs):
        """Format the results from vector store query"""
        return [
            {
                'content': doc.page_content,
                'source': doc.metadata['source']
            }
            for doc in docs
        ]
        
    def query_and_format(self, query_text, k=2):
        """Query vector DB and format results"""
        docs = self.query_vector_db(query_text, k)
        return self.format_results(docs)
