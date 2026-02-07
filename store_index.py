from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
from src.helper import (
    load_pdf_files,
    filter_to_minimal_docs,
    text_split,
    download_embeddings,
)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HUGGINGFACE_EMBEDDINGS_MODEL = os.getenv("HUGGINGFACE_EMBEDDINGS_MODEL")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# 1. Load Data
extracted_data = load_pdf_files(data_path="data/")
filtered_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filtered_data)

# 2. Get Embeddings
embeddings = download_embeddings(HUGGINGFACE_EMBEDDINGS_MODEL)

# 3. Pinecone Connection
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"

# 4. Create Index if it doesn't exist
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# 5. Store data in Pinecone
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks, embedding=embeddings, index_name=index_name
)
