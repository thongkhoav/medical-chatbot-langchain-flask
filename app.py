from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.callbacks.manager import get_openai_callback
from dotenv import load_dotenv
from pinecone import Pinecone
from src.prompt import *
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_EMBEDDINGS_MODEL = os.getenv("HUGGINGFACE_EMBEDDINGS_MODEL")

embeddings = download_embeddings(HUGGINGFACE_EMBEDDINGS_MODEL)
index_name = "medical-chatbot"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

docsearch = PineconeVectorStore.from_existing_index(
    embedding=embeddings, index_name=index_name
)

# Initialize retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})


chatModel = ChatOpenAI(model="gpt-4o-mini")


system_prompt = (
    "You are an Medical assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("human", "{input}")]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)
    with get_openai_callback() as cb:
        response = rag_chain.invoke({"input": msg})
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost}")
        print("Response : ", response["answer"])
        return str(response["answer"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
