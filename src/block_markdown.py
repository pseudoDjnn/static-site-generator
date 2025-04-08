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
    
    
def block_to_block_type(block):
    pass

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