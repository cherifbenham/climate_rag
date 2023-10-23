import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    return FAISS.from_documents(docs, embeddings)