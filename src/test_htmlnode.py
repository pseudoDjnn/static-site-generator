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
    node = LeafNode("p", "Hello World")
    self.assertEqual(node.to_html(), "<p>Hello World</p>")
  
  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click here", {"href": "https://www.example.com"})
    self.assertEqual(
      node.to_html(),
      '<a href="https://www.example.com">Click here</a>'
    )
  
  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hello World")
    self.assertEqual(node.to_html(), "Hello World")
  
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
  
  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><b>grandchild</b></span></div>"
      )
  
  def test_to_html_many_children(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "Italic text"),
        LeafNode(None, "Normal text")
      ]
    )
    self.assertEqual(
      node.to_html(),
      "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
    )
  
  def test_headings(self):
    node = ParentNode(
      "h2",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "Italic text"),
        LeafNode(None, "Normal text")
      ]
    )
    self.assertEqual(
      node.to_html(),
      "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>"
    )

if __name__=="__main__":
    unittest.main()