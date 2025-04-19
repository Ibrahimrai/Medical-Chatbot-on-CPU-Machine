# Script to load PDF data → embed → store in a FAISS vector DB

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Path to where the PDF files are stored
DATA_PATH = "data/"

# Path to save the FAISS vector database
DB_FAISS_PATH = "vectorstores/db_faiss"

# Function to create and store the vector database
def create_vector_db():
    # Load all PDFs from the data/ folder
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    print(f"✅ Found {len(documents)} documents.")

    # Split large documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Convert text chunks into embeddings (vectors) using HuggingFace model
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': 'cpu'}
    )

    # Create FAISS vector store from those text chunks
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)
    print("✅ Vector DB created and saved at", DB_FAISS_PATH)

# This line ensures the function only runs when the script is directly executed
if __name__ == '__main__':
    create_vector_db()
 