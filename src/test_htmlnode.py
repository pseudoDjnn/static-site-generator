import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    # Test case 1: No properties
    node1 = HTMLNode()
    self.assertEqual(node1.props_to_html(), "")
    
    node2 = HTMLNode(props={'href': "https://example.com"})
    self.assertEqual(node2.props_to_html(), ' href="https://example.com"')
    
    node3 = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    self.assertEqual(node3.props_to_html(), ' href="https://example.com" target="_blank"')

    node4 = HTMLNode(props={"data-test": ""})
    self.assertEqual(node4.props_to_html(), ' data-test=""')

  def test_repr(self):
    pass

if __name__=="__main__":
    unittest.main()