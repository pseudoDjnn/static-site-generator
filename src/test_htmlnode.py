import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode(
      "div",
      "Hello World",
      None,
      {"class": "greeting", "href": "https://www.example.com"}
    )
    self.assertEqual(
      node.props_to_html(),
      ' class="greeting" href="https://www.example.com"'
    )
  
  def test_values(self):
    pass

  def test_repr(self):
    pass
    

if __name__=="__main__":
    unittest.main()