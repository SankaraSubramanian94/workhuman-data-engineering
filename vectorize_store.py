from sentence_transformers import SentenceTransformer
import pinecone

# Initialize Pinecone
pinecone.init(api_key="YOUR_API_KEY")

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create Pinecone index if not exists
index_name = 'tech_support_index'
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=384)

index = pinecone.Index(index_name)

def vectorize_and_store(chunks):
    vectors = model.encode(chunks)
    metadata = [{"chunk_id": i, "text": chunk} for i, chunk in enumerate(chunks)]
    index.upsert([(str(i), vector, meta) for i, (vector, meta) in enumerate(zip(vectors, metadata))])

def process_document(text):
    from chunking import sentence_chunking
    chunks = sentence_chunking(text)
    vectorize_and_store(chunks)