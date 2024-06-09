# data_pipeline/chunking.py
from sentence_transformers import SentenceTransformer

def chunk_text(text, chunk_size=512):
    words = text.split()
    chunks = []
    chunk = []
    count = 0
    for word in words:
        count += len(word) + 1
        if count > chunk_size:
            chunks.append(' '.join(chunk))
            chunk = [word]
            count = len(word) + 1
        else:
            chunk.append(word)
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks

def embed_text(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings
