import unittest

from inline_markdown import split_nodes_delimiter

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
  def test_delimiter_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" word", TextType.TEXT)
      ],
      new_nodes
    )
  
  def test_delimiter_bold_double(self):
    node = TextNode(
      "This is text with a **bold** word and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" word and ", TextType.TEXT),
        TextNode("another", TextType.BOLD)
      ],
      new_nodes
    )
  
if __name__=="__main__":
  unittest.main()