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
    
  def test_delimiter_bold_multiword(self):
    node = TextNode(
      "This is text with a **bold word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold word", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("another", TextType.BOLD)
      ],
      new_nodes
    )
    
  def test_delimiter_italic(self):
    node= TextNode("This is text with an _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word", TextType.TEXT)
      ],
      new_nodes
    )
  
  def test_delimiter_bold_and_italic(self):
    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    self.assertEqual(
      [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
      ],
      new_nodes
    )

  def test_delimiter_code(self):
    node = TextNode("This is text with as a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(
      [
       TextNode("This is text with as a ", TextType.TEXT),
       TextNode("code block", TextType.CODE),
       TextNode(" word", TextType.TEXT)
      ],
      new_nodes
    )
  
if __name__=="__main__":
  unittest.main()