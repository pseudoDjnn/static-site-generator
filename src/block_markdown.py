from enum import Enum

from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

# Step 1: Define BlockType as an Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"
    
# Step 2: Collect the blocks with the for/loop
def markdown_to_blocks(markdown):
  # Split the markdown by double newlines
  blocks = markdown.split("\n\n")
  # New list will be created to clean up whitespace
  filtered_blocks = []
  # Run a loop for the .strip() to work
  for block in blocks:
        if block == "":
            continue
        block = block.strip()  # Remove spaces at beginning and end
        filtered_blocks.append(block)
  return filtered_blocks
    
# Step 3: Define the function to check the Enums
def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

# Step 4: This is out converter and converts a ful markdown document into a single HTMLNode
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    pass

def test_to_children(text):
    pass

def paragraph_to_html_node(block):
    pass

def heading_to_html_node(block):
    pass

def code_to_html_node(block):
    pass

def olist_to_html_node(block):
    pass

def ulist_to_html_node(block):
    pass

def quote_to_html_node(block):
    pass
