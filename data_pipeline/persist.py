# data_pipeline/persist.py
import os
from pinecone import Pinecone, ServerlessSpec

def save_chunks(document_id, chunks, embeddings):
    PINECONE_API_KEY = os.getenv('API-KEY')
    pc = Pinecone(api_key=PINECONE_API_KEY)

    index_name = 'document-chunks'
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

    index = pc.Index(index_name)

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        index.upsert([(f'{document_id}_{i}', embedding.tolist())])
