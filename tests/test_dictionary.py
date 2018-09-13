import unittest

from app.dictionary import dictinary

class DictTest(unittest.TestCase):

    def test_dictinary(self):
        generated_dictionary = dictinary(3,8)
        """test whether each value is the square of each key."""
        for key, value in generated_dictionary.items():
            self.assertEqual(value, key**2)
    
    def test_dictinary_string(self):
        self.assertEqual(dictinary('d',8), "Please use numbers(integers)")

if __name__== '__main__':
    unittest.main()