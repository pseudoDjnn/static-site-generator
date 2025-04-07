import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links, text_to_textnodes

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
    text = "This ![image](is missing a closing bracket"
    matches = extract_markdown_images(text)
    self.assertListEqual([], matches)
  
  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://example.com)"
    matches = extract_markdown_links(text)
    self.assertListEqual([("link", "https://example.com")], matches)

  def tets_multiple_links(self):
    text = (
      "Click here [example1](https://example.com) and [example2](https://example2.com)"
    )
    matches = extract_markdown_links(text)
    self.assertListEqual([
      ("example1", "https://exmaple.com"),
      ("example1", "https://example2.com")
      ], matches)
  
  def test_no_links(self):
    text = "This has no links, just words."
    matches = extract_markdown_links(text)
    self.assertListEqual([], matches)
    
  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
    
  def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ],
        new_nodes,
    )

  def test_text_to_textnodes(self):
    text = "This is **bold** and _italic_ with `code` and an ![image](https://example.com/img.jpg) and a [link](https://example.com)"
    
    nodes = text_to_textnodes(text)
    
    expected_nodes = [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" with ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://example.com")
    ]
    
    self.assertListEqual(expected_nodes, nodes)
  
if __name__=="__main__":
  unittest.main()