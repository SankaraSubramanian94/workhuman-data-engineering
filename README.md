# Tech Support AI Chatbot

## Overview
This project implements a data pipeline for a RAG-based AI chatbot designed to provide technical support for customers of a tech company specializing in consumer electronics. The pipeline processes text documents, chunks them, vectorizes the chunks, and stores them in a vector database.

## Features
- Sentence-based chunking of text documents.
- Vectorization of text chunks using SentenceTransformers.
- Storage of vectors in Pinecone for efficient retrieval.

## Setup

### Prerequisites
- AWS account
- Python 3.11+
- Docker
- Pinecone API key

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/SankaraSubramanian94/workhuman-data-engineering.git
    cd tech-support-chatbot
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up AWS services (S3, Lambda, SQS, etc.)

### Running the Pipeline
1. Upload a document to S3.
2. The ingestion Lambda function triggers and sends the document content to SQS.
3. The processing Lambda function processes the SQS message, chunks the text, vectorizes the chunks, and stores them in Pinecone.

### Testing
1. Run unit tests:
    ```sh
    python -m unittest discover
    ```

## Deployment
1. Use AWS CodePipeline for CI/CD.
2. Deploy Lambdas and other services using AWS CloudFormation or Terraform.

## Design Decisions
- **Sentence-Based Chunking:** Chosen to maintain context and coherence.
- **SentenceTransformers:** Used for effective vectorization of text chunks.
- **Pinecone:** Selected for efficient vector storage and similarity search.

## License
[MIT](LICENSE)