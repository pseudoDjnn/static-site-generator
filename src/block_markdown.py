from enum import Enum

from htmlnode import ParentNode, LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
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
        block = block.strip()  # Remove spaces at beginning and end
      filtered_blocks.append(block)
  return filtered_blocks
    
# Step 3: Define the function to check the Enums
def block_to_block_type(block):
    lines = block.split("\n")
    
    # Check 1: If it is a heading (1-6 '#' followed by a space)
    if block.startswith("# ", "## ", "### ", "##### ", "##### ", "###### "):
        return BlockType.HEADING
    # Check 2: If it is a code block (starts and ends with ```)
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    # Check 3: If it is a quote block (every line starts with '>')
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    # Check 4: If it is an unordered list (every line starts with '- ')
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    # Check if it's an ordered list (lines start with '1. ', '2. ', '3. ', etc...)
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH

# Step 4: This is out converter and converts a ful markdown document into a single HTMLNode
def markdown_to_html_node(markdown):
    pass

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
