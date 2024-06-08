import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from chunking import sentence_chunking

class TestChunking(unittest.TestCase):
    def test_chunking(self):
        text = "This is a test document. It contains multiple sentences. Here is another sentence."
        chunks = sentence_chunking(text)
        self.assertTrue(len(chunks) > 1)

if __name__ == '__main__':
    unittest.main()
