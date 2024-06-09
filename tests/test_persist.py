# tests/test_persist.py
import unittest
from data_pipeline.persist import save_chunks
import os
import pinecone

class TestPersist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PINECONE_API_KEY = os.getenv('3362760c-268d-4659-aabb-dc5a03db589d')
        pinecone.init(api_key=PINECONE_API_KEY, environment='us-east-1')
        cls.index_name = 'test-document-chunks'
        if cls.index_name not in pinecone.list_indexes():
            pinecone.create_index(cls.index_name, dimension=384)
        cls.index = pinecone.Index(cls.index_name)

    def test_save_chunks(self):
        chunks = ["chunk1", "chunk2"]
        embeddings = [[0.1] * 384, [0.2] * 384]
        save_chunks(1, chunks, embeddings)
        results = self.index.query(queries=[[0.1] * 384], top_k=1)
        self.assertGreater(len(results['matches']), 0)

    @classmethod
    def tearDownClass(cls):
        cls.index.delete(delete_all=True)
        pinecone.delete_index(cls.index_name)

if __name__ == '__main__':
    unittest.main()
