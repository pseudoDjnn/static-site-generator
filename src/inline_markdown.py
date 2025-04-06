import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    # If our node is already special (not plain TEXT), just add it the output
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    
    # This is for the TEXT node
    split_nodes = []
    # Use built in split function with our delimiter argument
    sections = old_node.text.split(delimiter)
    
    """ 
    Check to see if we have valid markdown 
    There should be an odd number of sections
    (text, delimit, text, delimit, text) as pattern
    """
    if len(sections) % 2 == 0:
      raise ValueError("invalid markdown, formatted section not closed")
    
    # Process each section
    for i in range(len(sections)):
      # Skip the empty sections
      if sections[i] == "":
        continue
      
      # As stated above, anything 'even' will be regular text
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], TextType.TEXT))
      # Our odd-indexed sections are special and will return our text_type argument
      else:
        split_nodes.append(TextNode(sections[i], text_type))
        
        # Add all the split nodes to our result list
    new_nodes.extend(split_nodes)
  return new_nodes

def extract_markdown_images(text):
  # Define the regex Pattern
  pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  
  # Use re.findall to dynamically extract matches from the given text
  matches = re.findall(pattern, text)

  # Return the list of tuples (alt text, URL)
  return matches

def extract_markdown_links(text):
  # Same as above and just regex for the links this time
  pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  
  matches = re.findall(pattern, text)

  # Return the list of tuples (anchor text, URL)
  return matches

def split_nodes_image(old_nodes):
  pass

def split_nodes_links(old_nodes):
  pass