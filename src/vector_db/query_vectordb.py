
# query_vectordb.py: import os\nfrom dotenv import load_dotenv\nfrom langchain.embeddings.openai import OpenAIEmbeddings\nfrom langchain.vectorstores import FAISS\n\n# Load environment variables\nload_dotenv()\n\n# Initialize the OpenAI embeddings\nembeddings = OpenAIEmbeddings()\n\n# Load the vector store\nvector_store = FAISS.load_local(\"faiss_index\", embeddings)\n\n# Function to query the vector store\ndef query_vector_db(query_text, k=2):\n    # Search for similar documents\n    docs = vector_store.similarity_search(query_text, k=k)\n    \n    print(f\"\\nQuery: {query_text}\")\n    print(\"\\nResults:\")\n    for i, doc in enumerate(docs):\n        print(f\"\\n{i+1}. {doc.page_content}\")\n        print(f\"   Source: {doc.metadata['source']}\")\n\n# Test with some queries\nquery_vector_db(\"How do vector databases work?\")\nquery_vector_db(\"What is cosine similarity?\")\nquery_vector_db(\"What can I use vector databases for?\")"

import os
from langchain import hub
from dotenv import load_dotenv

from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from vector_db.create_vectordb import VectorDB


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
   {"context": VectorDB.get_vector_db_retriever, "question": RunnablePassthrough()}
   | prompt
   | llm
   | StrOutputParser()
)

# Question
rag_chain.invoke("What is the steps for creating a simple CLI LangChain chat app?")

