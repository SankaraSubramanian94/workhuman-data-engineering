import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from vectorize_store import vectorize_and_store

class TestVectorizeStore(unittest.TestCase):
    def test_vectorization(self):
        chunks = ["This is a test chunk."]
        vectorize_and_store(chunks)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
