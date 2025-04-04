import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images

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
    
  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    matches = extract_markdown_images(text)
    self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
  def test_multiple_images(self):
    text = (
      "Here is one image ![first](https://example.com/first.png) "
      "and the second ![second](https://example.com/second.jpg)."
    )
    matches = extract_markdown_images(text)
    self.assertEqual([
      ("first", "https://example.com/first.png"),
      ("second", "https://example.com/second.jpg")
    ], matches)

  def test_no_images(self):
    text = "This is just text, no image at all"
    matches = extract_markdown_images(text)
    self.assertListEqual([], matches)
  
  def test_malformed_image(self):
    pass
  
if __name__=="__main__":
  unittest.main()