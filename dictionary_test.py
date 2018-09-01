import unittest

from dictionary import dictinary

class DictTest(unittest.TestCase):

    def test_dictinary(self):
        self.assertEqual(dictinary(3,8), {3: 9, 4: 16, 5: 25, 6: 36, 7: 49})
    
    def test_dictinary_string(self):
        self.assertEqual(dictinary('d',8), "Please use numbers(integers)")

if __name__== '__main__':
    unittest.main()