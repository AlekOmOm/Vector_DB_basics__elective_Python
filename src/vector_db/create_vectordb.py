

# file: to convert sample data to vectors and save them"
##       "code": "# create_vectordb.py\n\nimport os\nfrom dotenv import load_dotenv\nfrom langchain.embeddings.openai import OpenAIEmbeddings\nfrom langchain.vectorstores import FAISS\nfrom langchain.schema import Document\nfrom sample_data import documents\n\n# Load environment variables\nload_dotenv()\n\n# Initialize the OpenAI embeddings\nembeddings = OpenAIEmbeddings()\n\n# Convert the sample texts to Document objects\ndocs = [Document(page_content=text, metadata={\"source\": f\"doc_{i}\"}) for i, text in enumerate(documents)]\n\n# Create and save the vector store locally\nvector_store = FAISS.from_documents(docs, embeddings)\nvector_store.save_local(\"faiss_index\")\n\nprint(\"Vector database created and saved successfully!\")"

import os
from env.secrets_manager import SecretsManager

from dotenv import load_dotenv


from langchain_community.embeddings import OpenAIEmbeddings


from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from data import sample_data # sample_data.py at location: ~/data/sample_data.py



class VectorDB:
   def __init__(self):
        self.vector_store = None
        self.retriever = None

   def create_vector_db(self):
      self.load_environment_variables()
      self.init_embeddings()
      self.init_docs()
      
      # Create and save the vector store locally
      self.vector_store = FAISS.from_documents(self.docs, self.embeddings)
      self.vector_store.save_local("./faiss_index_db") # save the vector store locally

      self.retriever = self.vector_store.retriever

      print("Vector database created and saved successfully!")

   def load_environment_variables(self):
      os.environ['LANGCHAIN_API_KEY'] = SecretsManager.get_secret("Langchain_API_Key", "credential", "API_Keys")
      os.environ['OPENAI_API_KEY'] = SecretsManager.get_secret("OpenAI_API_Key", "credential", "API_Keys")
      os.environ['LANGCHAIN_TRACING_V2'] = 'true'
      os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
      os.environ['LANGSMITH_PROJECT'] = "Python RAG undervisning"

      load_dotenv()

   def init_embeddings(self):
      # Initialize the OpenAI embeddings
      self.embeddings = OpenAIEmbeddings(
         api_key=SecretsManager.get_secret("OpenAI_API_Key", "credential", "API_Keys"),
         model="gpt-3.5-turbo"
      )
   
   def init_docs(self):
      self.docs = [Document(page_content=text, metadata={"source": f"doc_{i}"}) for i, text in enumerate(sample_data.documents)]
   
   def get_vector_db_retriever(self):
      self.create_vector_db()
      return self.retriever
   

if __name__ == "__main__":
   vectordb = VectorDB()
   vectordb.create_vector_db()
   retriever = vectordb.get_vector_db_retriever()
   print(retriever)
