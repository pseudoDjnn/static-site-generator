import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    # Test case 1: No properties
    node1 = HTMLNode()
    self.assertEqual(node1.props_to_html(), "")
    
    # Test case 2: Single property
    node2 = HTMLNode(props={'href': "https://example.com"})
    self.assertEqual(node2.props_to_html(), ' href="https://example.com"')
    
    # Test case 3: Multiple properties
    node3 = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    self.assertEqual(node3.props_to_html(), ' href="https://example.com" target="_blank"')

    # Test case 4: Empty string value
    node4 = HTMLNode(props={"data-test": ""})
    self.assertEqual(node4.props_to_html(), ' data-test=""')

  def test_repr(self):
    # Test case 1: Empty node
    node1 = HTMLNode()
    self.assertEqual(
      repr(node1),
      "HTMLNode(tag=None, value=None, children=0, props=None)"
    )
    
    # Test case 2: Node with tag, value, props
    node2 = HTMLNode(tag="p", value="Hello World", props={"class": "exmaple-class"})
    self.assertEqual(
      repr(node2),
      "HTMLNode(tag='p', value='Hello World', children=0, props={'class': 'exmaple-class'})"
    )
    
    
class TestLeafNode(unittest.TestCase):
  # Test case 1: A 'p' tag
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello world!")
    self.assertEqual(node.to_html(), "<p>Hello world!</p>")
    
  # Test case 2: An 'a' tag with 'href' prop
  def test_leaf_to_html_a_with_href(self):
    node = LeafNode("a", "Click here", props={"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here</a>')
  
  # Test case 3: No tag
  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Just text")
    self.assertEqual(node.to_html(), "Just text")
  
  # Test case 4: Raise 'ValueError' when 'value' is None
  def test_leaf_to_html_no_value(self):
    with self.assertRaises(ValueError):
      LeafNode("p", None)
      
      
class TestParentNode(unittest.TestCase):
  # Test case 1: Single 'child'
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
  
  # Test case 2: First nesting
  def test_to_html_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><b>grandchild</b></span></div>"
    )
    

if __name__=="__main__":
    unittest.main()