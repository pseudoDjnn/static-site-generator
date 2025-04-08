import unittest
from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_makrdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items"
            ]
        )
        
    def test_markdown_to_blocks_with_multiple_newlines(self):
        md = """
# Heading


This paragraph has multiple newlines above it.



- List item 1
- List item 2


> This is a blockquote
        """
        blocks = markdown_to_blocks(md)        
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "This paragraph has multiple newlines above it.",
                "- List item 1\n- List item 2",
                "> This is a blockquote"
            ]
        )


if __name__=="__main__":
    unittest.main()