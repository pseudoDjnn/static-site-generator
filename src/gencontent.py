import os
from markdown_blocks import markdown_to_html_node

def generate_pages(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

def extract_title(markdown):
    # Break the markdown into individual lines
    lines = markdown.split("\n")
    
    # Iterate through each line
    for line in lines:
        # Check if the line starts with `#`
        if line.startswith("# "):
            return line[2:]
    # If no `h1` is found, raise error
    raise ValueError("No title found")