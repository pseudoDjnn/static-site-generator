import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        text = extract_title("# This is a title")
        self.assertEqual(text, "This is a title")
    
    def test_eq_double(self):
        text = extract_title(
        """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(text, "This is a title")
        
    def test_eq_long(self):
        pass
    
    def test_none(self):
        pass

if __name__=="__main__":
    unittest.main()