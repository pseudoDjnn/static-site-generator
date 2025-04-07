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
  # create the same empty list as delimiter list
  new_nodes = []

  # Run our loop for the input
  for old_node in old_nodes:
    #  Just following the same format we did with the split above
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    
    # Extract images from the text we write
    images = extract_markdown_images(old_node.text)

    # If we have no images, just add the original ndoe
    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    
    # Start again with the full text
    remaining_text = old_node.text
    
    for alt_text, url in images:
      # Create the full image markdown pattern to split on
      image_markdown = f"![{alt_text}]({url})"
      
      # Split the text into 'before image' and 'after image'
      parts = remaining_text.split(image_markdown, 1)
      
      # The text before the image
      before_text = parts[0]
      
      # Add a node for the text before the image (if not empty)
      if before_text:
        new_nodes.append(TextNode(before_text, TextType.TEXT))
        
      # Add a node for the image itself
      new_nodes.append(TextNode(alt_text,TextType.IMAGE, url))

      # Update remaining_text to be everything after the image
      if len(parts) > 1:
        remaining_text = parts[1]
      else:
        remaining_text = ""

    # Add any remaining text after the last image (if not empty) 
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))
      
  return new_nodes

def split_nodes_links(old_nodes):
    # create the same empty list as delimiter list
  new_nodes = []

  # Run our loop for the input
  for old_node in old_nodes:
    #  Just following the same format we did with the split above
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    
    # Extract images from the text we write
    images = extract_markdown_links(old_node.text)

    # If we have no images, just add the original ndoe
    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    
    # Start again with the full text
    remaining_text = old_node.text
    
    for text, url in images:
      # Create the full image markdown pattern to split on
      image_markdown = f"[{text}]({url})"
      
      # Split the text into 'before image' and 'after image'
      parts = remaining_text.split(image_markdown, 1)
      
      # The text before the image
      before_text = parts[0]
      
      # Add a node for the text before the image (if not empty)
      if before_text:
        new_nodes.append(TextNode(before_text, TextType.TEXT))
        
      # Add a node for the image itself
      new_nodes.append(TextNode(text,TextType.LINK, url))

      # Update remaining_text to be everything after the image
      if len(parts) > 1:
        remaining_text = parts[1]
      else:
        remaining_text = ""

    # Add any remaining text after the last image (if not empty) 
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))
      
  return new_nodes


def text_to_textnodes(text):
  # Start with a list containing one TextNode with the entire text
  nodes = [TextNode(text, TextType.TEXT)]

  # Apply each splitting function in sequence
  nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_links(nodes)
  
  return nodes