import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    # Test case 1: No properties
    node1 = HTMLNode()
    assert node1.props_to_html() == ""

  def test_repr(self):
    pass

if __name__=="__main__":
    unittest.main()