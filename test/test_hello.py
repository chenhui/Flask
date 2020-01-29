import unittest
from  flask import escape

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_escape(self):
        self.assertEqual('chenlaoshi',escape('chenlaoshi'))

if __name__ == '__main__':
    unittest.main()