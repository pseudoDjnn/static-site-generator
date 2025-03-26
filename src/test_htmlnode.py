import unittest

from htmlnode import HTMLNode, LeafNode


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
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello world!")
    self.assertEqual(node.to_html(), "<p>Hello world!</p>")

if __name__=="__main__":
    unittest.main()