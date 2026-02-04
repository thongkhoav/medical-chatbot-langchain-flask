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

## Project Structure Notes

### The `*.egg-info` Folder

After installing the project dependencies (specifically when running `-e .` in `requirements.txt`), a folder named `medical_chatbot.egg-info` will be created.

- **What it is:** This contains metadata about your local package, allowing you to use absolute imports like `from src.helper import ...`.
- **Note:** This folder is **auto-generated** and is already included in `.gitignore`. You do not need to commit it or manually modify its contents.
