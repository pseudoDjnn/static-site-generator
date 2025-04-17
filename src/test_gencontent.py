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
        text = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(text, "title")
    
    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

if __name__=="__main__":
    unittest.main()