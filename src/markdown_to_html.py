from htmlnode import HTMLNode, ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

def create_paragraph_node(text):
    return ParentNode(tag="p", children=[LeafNode(tag=None, value=text)])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = create_paragraph_node(block)

        else:
            continue
        
        all_nodes.append(node)

    return ParentNode(tag="div", children=all_nodes)