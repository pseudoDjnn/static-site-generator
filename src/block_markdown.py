import re
from enum import Enum

# Step 1: Define BlockType as an Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
# Step 2: Define the function to check the Enums
def block_to_block_type(block):
    # Check 1: If it is a heading (1-6 '#' followed by a space)
    if block.startswidth("#"):
        return BlockType.HEADING
    
    # Check 2: If it is a code block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check 3: If it is a quote block (every line starts with '>')
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    
    
    
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
  # Split the markdown by double newlines
  blocks = markdown.split("\n\n")
  
  # New list will be created to clean up whitespace
  cleaned_blocks = []
  # Run a loop for the .strip() to work
  for block in blocks:
    cleaned_block = block.strip()  # Remove spaces at beginning and end
    if cleaned_block:  # Only keep non-empty blocks
      cleaned_blocks.append(cleaned_block)
      
  return cleaned_blocks