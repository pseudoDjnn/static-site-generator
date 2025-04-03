import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    sections = old_node.text.split(delimiter)
    if len(sections) % 2 == 0:
      raise ValueError("invalid markdown, formatted section not closed")
    for i in range(len(sections)):
      if sections[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], TextType.TEXT))
      else:
        split_nodes.append(TextNode(sections[i], text_type))
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