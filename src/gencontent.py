import os
from markdown_blocks import markdown_to_html_node

def generate_pages(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

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