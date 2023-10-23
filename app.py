import gradio as gr
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
from loader import load_documents
from preprocessor import preprocess_content
from chatbot import chatbot
from splitter import split_documents_into_chunks
from search import nearest_neighbors
from utils import prettify

# --- choosing a folder ---
directory_path = "data/"

# --- loading the pdf documents ---
docs = load_documents(directory_path)

# --- preprocess the data ---
for doc in docs:
    doc.page_content = preprocess_content(doc.page_content)

# --- choose a text_splitter ---
text_splitter = SentenceTransformersTokenTextSplitter(tokens_per_chunk=384, chunk_overlap=0)

# --- split the docs into smaller chunks ---
new_docs = split_documents_into_chunks(docs, text_splitter)

# --- load the vectorstore ---
from vectorstore import create_vectorstore
vectorstore = create_vectorstore(new_docs)

# --- Gradio App ---
def app(query):
    system_context = nearest_neighbors(query, vectorstore, k=5)
    return chatbot(query, prettify(system_context))

iface = gr.Interface(fn=app, inputs="text", outputs="text")
iface.launch(share=True)
