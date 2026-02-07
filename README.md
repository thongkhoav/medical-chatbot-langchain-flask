# medical-chatbot-langchain-flask

## Development Setup

1. Create and activate a conda environment (Conda is preferred over pip as it manages non-Python dependencies and provides more robust environment isolation):

   ```bash
   conda env create -f environment.yml
   conda activate medical-chatbot
   conda list
   conda deactivate
   ```

2. Install dependencies:

   **Option 1: The "Quick" Way (Recommended)**
   If you just added a few new libraries to `requirements.txt`, run this inside your activated environment:

   ```bash
   pip install -r requirements.txt
   ```

   This is the fastest method. `pip` will look at what's already installed and only download the new packages you added.

3. Set up pre-commit hooks (optional but recommended for code quality and style):

   ```bash
   pre-commit install
   ```

## Running the Application

### 1. Store the Index (First Time Only)

Before running the app, you need to process your PDF and store the embeddings in Pinecone:

```bash
python store_index.py
```

### 2. Run the Web App

Finally, start the Flask server:

```bash
python app.py
```

The application will be available at `http://localhost:8080`.

> **Note:** If you see an "Address already in use" error, it means another process is using port 8080. You can either stop that process or change the port in `app.py`.

## Vector Database

This project currently uses **Pinecone** as a remote vector database for storing and retrieving medical document embeddings.

### Why Pinecone?

- **Serverless & Remote:** No need to manage local database files or memory.
- **Scalability:** Handles large amounts of vector data efficiently.
- **Performance:** High-speed similarity search in the cloud.

### Local Alternative: ChromaDB

If you prefer to run the project entirely offline or without a Pinecone API key, you can swap the implementation to use **ChromaDB**.

- **Local:** Databases are stored as files on your local machine.
- **Free:** No cloud costs or API limits.
- **Privacy:** Data never leaves your hardware.

To switch to Chroma, you would need to install `langchain-chroma` and update the vector store initialization in `src/helper.py`.

## Project Structure Notes

### The `*.egg-info` Folder

After installing the project dependencies (specifically when running `-e .` in `requirements.txt`), a folder named `medical_chatbot.egg-info` will be created.

- **What it is:** This contains metadata about your local package, allowing you to use absolute imports like `from src.helper import ...`.
- **Note:** This folder is **auto-generated** and is already included in `.gitignore`. You do not need to commit it or manually modify its contents.
