from htmlnode import HTMLNode, ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

def create_paragraph_node(text):
    return ParentNode(tag="p", children=[LeafNode(tag=None, value=text)])

def create_heading_node(text):
    # Count the number of leading '#' for the heading level
    heading_level = len(text) - len(text.lstrip("#"))
    if heading_level < 1 or heading_level > 6:
        raise ValueError("Invalid heading level")

    # Remove the '#' characters and strip whitespace
    heading_text = text.lstrip('#').strip()

    # Create and return the LeadNode for the heading
    return LeafNode(tag=f"h{heading_level}", value=heading_text)

def create_quote_node(text):
    cleaned_text = text.lstrip('>').strip()

    # Wrap and make sure to use 'blockquote'
    return ParentNode(tag="blockquote", children=[LeafNode(tag=None, value=cleaned_text)])

def create_code_node(text):
    if text.startswith("```") and text.endswith("```"):
        cleaned_text = text[3:-3].strip()
    else:
        raise ValueError("Text must start and end with triple backticks")
        
    return ParentNode(tag="pre", children=[LeafNode(tag="code", value=cleaned_text)])

def create_unordered_list_node(text):
    pass

def create_ordered_list_node(text):
    pass

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = create_paragraph_node(block)
        elif block_type == BlockType.HEADING:
            node = create_heading_node(block)
        elif block_type == BlockType.QUOTE:
            node = create_quote_node(block)
        elif block_type == BlockType.CODE:
            node = create_code_node(block)

        else:
            print(f"Warning: Unhandled block type {block_type}")
            continue    # Skip unhandled block tpyes for now
        
        all_nodes.append(node)

    # Wrap all nodes in a single parent <div>
    return ParentNode(tag="div", children=all_nodes)