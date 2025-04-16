def extract_title(markdown):
    # Break the markdown into individual lines
    lines = markdown.split("\n")
    
    # Iterate through each line
    for line in lines:
        # Check if the line starts with `#`
        if line.starswith("# "):
            return line[2:]
    # If no `h1` is found, raise error
    raise ValueError("No title found")