---
description: General project guidelines for Medical Chatbot regarding RAG stack, security, and code quality.
globs: "**/*"
alwaysApply: true
---

# Medical Chatbot Project Rules

## Environment & Jupyter Notebooks

- **Kernel Matching**: When using Jupyter notebooks, you MUST select the kernel and interpreter to be the same to avoid import resolution issues.

## Technology Stack

- **Architecture**: RAG (Retrieval-Augmented Generation) for chatbot.
- **Core Components**:
  - Flask (Web Framework)
  - Python (Language)
  - LangChain (Orchestration)
  - OpenAI (LLM)
  - Pinecone (Vector Database)

## Security & Configuration

- **No Secrets**: Do NOT commit sensitive keys (API keys, tokens) to the source code.
- **Environment Template**: When a new environment variable is created, you MUST add it to `.env.example` with a placeholder value.

## Code Quality

- **No Magic Values**: Do not create magic numbers or magic strings. Always assign them to a named variable with a descriptive name.
