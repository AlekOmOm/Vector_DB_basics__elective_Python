

# file: to convert sample data to vectors and save them"
##       "code": "# create_vectordb.py\n\nimport os\nfrom dotenv import load_dotenv\nfrom langchain.embeddings.openai import OpenAIEmbeddings\nfrom langchain.vectorstores import FAISS\nfrom langchain.schema import Document\nfrom sample_data import documents\n\n# Load environment variables\nload_dotenv()\n\n# Initialize the OpenAI embeddings\nembeddings = OpenAIEmbeddings()\n\n# Convert the sample texts to Document objects\ndocs = [Document(page_content=text, metadata={\"source\": f\"doc_{i}\"}) for i, text in enumerate(documents)]\n\n# Create and save the vector store locally\nvector_store = FAISS.from_documents(docs, embeddings)\nvector_store.save_local(\"faiss_index\")\n\nprint(\"Vector database created and saved successfully!\")"

import os
from env.secrets_manager import SecretsManager
from langchain import hub
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain.schema import Document
from data import sample_data # sample_data.py at location: ~/data/sample_data.py


os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGSMITH_PROJECT'] = "Python RAG undervisning"

os.environ['LANGCHAIN_API_KEY']
os.environ['OPENAI_API_KEY']


# Load environment variables (for non-secret config)
load_dotenv()

# Get API keys from 1Password
openai_api_key = SecretsManager.get_secret("OpenAI_API_Key", "credential", "API_Keys")
langchain_api_key = SecretsManager.get_secret("Langchain_API_Key", "credential", "API_Keys")

# init embeddings
embeddings = OpenAIEmbeddings(
   api_key=os.getenv("OPENAI_API_KEY"),
   model="gpt-3.5-turbo"
)

# init vector_store
vector_store = FAISS.from_documents(
   docs=sample_data.documents,
   embedding_func=embeddings,
   persist_dir="./faiss_langchain_db" # local storage
)

retriever = vector_store.retriever

#### RETRIEVAL and GENERATION ####

# prompt 
prompt = hub.pull("rlm/rag-prompt")


# LLM 
llm = ChatOpenAI(
   model_name="gpt-3.5-turbo",
   temperature=0.0
)

# Chain
rag_chain = (
   {"context": retriever, "question": RunnablePassthrough()}
   | prompt
   | llm
   | StrOutputParser()
)

# Question
rag_chain.invoke("What is the steps for creating a simple CLI LangChain chat app?")


