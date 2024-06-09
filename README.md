# Data Pipeline

## Overview
The data pipeline components are responsible for processing and managing text data within the FastAPI application. This includes chunking long texts into smaller segments, generating embeddings for the text chunks, and persisting the processed data to a vector database.

## Components

### chunking.py
The `chunking.py` module provides functionality for breaking down long texts into smaller chunks and generating embeddings for the chunks.

- **`chunk_text(text, chunk_size=512)`:** Function to split a long text into smaller chunks based on a specified maximum size. It aggregates sentences into chunks to ensure manageable segment sizes.

- **`embed_text(text)`:** Function to generate embeddings for text chunks using a pre-trained SentenceTransformer model. Embeddings capture semantic meaning and are useful for downstream analysis.

### persist.py
The `persist.py` module handles the persistence of processed data to a vector database (e.g., Pinecone). It provides functions for saving text chunks and their embeddings to the database.

- **`save_chunks(document_id, chunks, embeddings)`:** Function to save text chunks and their corresponding embeddings to the vector database. It creates an index for storing the data and uses Pinecone's API for data storage and retrieval.

### process_input.py
The `process_input.py` script serves as an entry point for processing input text data. It reads input from a file, processes the text using the chunking and embedding functions, and persists the processed data to the vector database.

- **Usage:** `python process_input.py --document_id <document_id> --file_path <file_path>`

## Setup and Usage
1. **Environment Setup**: Ensure Python and necessary dependencies are installed (`requirements.txt`).
2. **Configuration**: Set up environment variables for database connection details and API keys (e.g., Pinecone API key).
3. **Run Process Input Script**: Use the `process_input.py` script to process input text data and persist it to the vector database.