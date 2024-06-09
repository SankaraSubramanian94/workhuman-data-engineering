# process_input.py
import os
import argparse
import pdfplumber
from data_pipeline.chunking import chunk_text, embed_text
from data_pipeline.persist import save_chunks

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_file(document_id, file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)
    save_chunks(document_id, chunks, embeddings)
    print(f"Processed {len(chunks)} chunks from the file '{file_path}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an input file, chunk it, and save embeddings.')
    parser.add_argument('document_id', type=int, help='The document ID')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    
    args = parser.parse_args()
    process_file(args.document_id, args.file_path)
