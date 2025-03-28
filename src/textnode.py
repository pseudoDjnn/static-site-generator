from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
                )
        

    def text_node_to_html_node(self, text, text_node):

        if not isinstance(text_node, TextNode):
            raise TypeError("Expected a TextNode instance")
        
        match (text_node, text_node.text_type):
            case TextType.TEXT:
                return LeafNode('', text)
            case TextType.BOLD:
                return LeafNode('b', text)
            case TextType.ITALIC:
                return LeafNode('i', text)
            case TextType.CODE:
                return LeafNode('code', text)
            case _:
                raise Exception("Only us valid TextTypes")
    

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
