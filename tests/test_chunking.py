# tests/test_chunking.py
import unittest
from data_pipeline.chunking import chunk_text, embed_text

class TestChunking(unittest.TestCase):

    def test_chunk_text(self):
        text = "This is a test. This is only a test."
        chunks = chunk_text(text, chunk_size=10)
        self.assertEqual(len(chunks), 2)
        self.assertEqual(chunks[0], "This is a test.")
        self.assertEqual(chunks[1], "This is only a test.")
    
    def test_embed_text(self):
        text = ["This is a test.", "This is only a test."]
        embeddings = embed_text(text)
        self.assertEqual(len(embeddings), 2)
        self.assertEqual(len(embeddings[0]), 384)  # Dimension of 'all-MiniLM-L6-v2'

if __name__ == '__main__':
        unittest.main()
