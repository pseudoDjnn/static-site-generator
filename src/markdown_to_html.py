from htmlnode import HTMLNode, ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type

def create_paragraph_node(text):
    return ParentNode(tag="p", children=[LeafNode(tag=None, value=text)])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []

    for block in blocks:
        pass

    return ParentNode(tag="div", children=all_nodes)