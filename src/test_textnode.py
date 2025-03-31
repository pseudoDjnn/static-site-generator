import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node",TextType.TEXT)
        self.assertEqual(node, node2)
        
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode("Link text", TextType.TEXT, "https://example.com")
        node2 = TextNode("Link text", TextType.TEXT, "https://different-site.com")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.example.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.example.com)", repr(node)
            )
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        pass
    def test_image(self):
        pass
    def test_bold(self):
        pass

if __name__=="__main__":
    unittest.main()
