# src/vector_db/repository.py

from langchain_community.vectorstores import FAISS

class VectorDBRepository:
    _instance = None

    @classmethod 
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.vector_store = None 

    def create_vector_store(self, documents, embeddings):
        """Create a new vector store from documents"""
        self.vector_store = FAISS.from_documents(documents, embeddings)
        return self.vector_store

    def save_vector_store(self, path="faiss_index"):
        """Save the vector store to disk"""
        if self.vector_store:
            self.vector_store.save_local(path)
            return True
        return False

    
    def load_vector_store(self, path="faiss_index", embeddings=None):
        """Load the vector store from disk"""
        if not self.vector_store:
            self.vector_store = FAISS.load_local(path, embeddings) 
        return self.vector_store

    def get_vector_store(self):
        """Get the current vector store instance"""
        return self.vector_store
    




