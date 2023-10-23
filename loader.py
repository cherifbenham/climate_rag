import os
from langchain.document_loaders import PyPDFLoader


# --- Load Docs from Directory ---
def load_documents(directory_path):
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    documents = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory_path, pdf_file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())
    return documents
