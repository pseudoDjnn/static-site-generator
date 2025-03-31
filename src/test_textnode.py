import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Lorem ipsum dolor sit amet", TextType.TEXT)
        node2 = TextNode("Lorem ipsum dolor sit amet",TextType.TEXT)
        self.assertEqual(node, node2)
        
    def test_eq_false(self):
        node = TextNode("Lorem ipsum dolor sit amet", TextType.TEXT)
        node2 = TextNode("Lorem ipsum dolor sit amet", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq_false2(self):
        node = TextNode("Lorem ipsum dolor sit amet", TextType.TEXT)
        node2 = TextNode("Lorem ipsum dolor sit amet,", TextType.TEXT)
        self.assertNotEqual(node, node2)
        
    def test_eq_url(self):
        node = TextNode("Link text", TextType.TEXT, "https://example.com")
        node2 = TextNode("Link text", TextType.TEXT, "https://different-site.com")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("Lorem ipsum dolor sit amet", TextType.TEXT, "https://www.example.com")
        self.assertEqual(
            "TextNode(Lorem ipsum dolor sit amet, text, https://www.example.com)", repr(node)
            )
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("Lorem ipsum dolor sit amet", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Lorem ipsum dolor sit amet")
        
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.example.com", "alt": "This is an image"}
        )
    
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__=="__main__":
    unittest.main()
