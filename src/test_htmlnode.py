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
    node = HTMLNode(
      "div",
      "Lorem ipsum dolor sit amet"
    )
    self.assertEqual(
      node.tag,
      "div"
    )
    self.assertEqual(
      node.value,
      "Lorem ipsum dolor sit amet"
    )
    self.assertEqual(
      node.children,
      None
    )
    self.assertEqual(
      node.props,
      None
    )

  def test_repr(self):
    node = HTMLNode(
      "p",
      "Lorem ipsum",
      None,
      {"class": "primary"}
    )
    self.assertEqual(
      node.__repr__(),
      "HTMLNode(p, Lorem ipsum, children: None, {'class': 'primary'})"
    )
    
    # Testing the leaf nodes
    def test_leaf_to_html_p(self):
      pass
    
    def test_leaf_to_html_a(self):
      pass
    
    def test_leaf_to_html_no_tag(self):
      pass
    
    def tets_to_html_with_children(self):
      pass
    
    def test_to_html_with_grandchildren(self):
      pass
    
    def test_to_html_many_children(self):
      pass
    
    def tets_headings(self):
      pass

if __name__=="__main__":
    unittest.main()