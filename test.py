import unittest
from goodness_measures import ngrams, substring_reduction, accessor_variety, description_length_gain


class TestBpe(unittest.TestCase):

    def test_ngrams(self):
        l = "the door handle is broken where can i buy a new door handle ."
        expected = {'the door': 1, 'door handle': 2, 'handle is': 1,
                    'is broken': 1, 'broken where': 1,
                    'where can': 1, 'can i': 1, 'i buy': 1, 'buy a': 1,
                    'a new': 1, 'new door': 1, 'handle .': 1}
        assert ngrams(l, 2) == expected

    def test_substring_reduction(self):
        l = "the door handle is broken because where can i buy a new door handle ."
        expected = ['door handle']
        assert substring_reduction(l) == expected

    def test_accessor_variety(self):
        l = ""
        expected = []
        assert accessor_variety(l) == expected

    def test_description_length_gain(self):
        l = ""
        expected = []
        assert description_length_gain(l) == expected

if __name__ == "__main__":
	unittest.main()
