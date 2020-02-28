import unittest
from reduction import ngrams, substring_reduction

class TestBpe(unittest.TestCase):

    def test_ngrams(self):
        l = "the door handle is broken because where can i buy a new door handle ."
        expected = {'the door': 1, 'door handle': 2, 'handle is': 1, 
                    'is broken': 1, 'broken because': 1, 'because where': 1, 
                    'where can': 1, 'can i': 1, 'i buy': 1, 'buy a': 1, 
                    'a new': 1, 'new door': 1, 'handle .': 1}
        assert ngrams(l, 2) == expected

    def test_substring_reduction(self):
        l = "the door handle is broken because where can i buy a new door handle ."
        assert substring_reduction(l) == ['door handle']

        
if __name__ == "__main__":
	unittest.main()