class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props
      
    def to_html(self):
      raise NotImplementedError
    
    def props_to_html(self):
      if not self.props:  #  Check for None or empty dictionary
        return ""
      
      # Use list comphrehension to generate a list of ' key="value"' strings
      attributes = [f' {key}="{value}"' for key, value in self.props.items()]
      
      # Join the list into a single string and return it
      return "".join(attributes)
    
    def __repr__(self):
      return (
        f"HTMLNode(tag={self.tag!r}, "
        f"value={self.value!r}, "
        f"children={len(self.children) if self.children else 0}, "
        f"props={self.props})"
      )
      
class LeafNode(HTMLNode):
  # Make 'value' mandatory
  def __init__(self, tag, value, props=None):
    # Make sure 'children' set to None
    super().__init__(tag, value=value, children=None, props=props)
    
    
  def to_html(self):
    # Check that value isn't None
    if self.value is None:
      raise ValueError("All leaf nodes must have a value")
    # Just render text if we have no 'tag'
    if not self.tag:
      return self.value
    
    # Return the full HTML tag with props and vlaue
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  
class ParentNode(HTMLNode):
  # Make tag and children mandatory and props optional
  def __init__(self, tag, children, props=None):
    super().__init__(tag, children, props=props)
    
  # First recursive call
  def to_html(self):
    # Check to see it meets our requirements 
    if self.tag is None:
      raise ValueError("All parent nodes must have a tag")
    
    if self.children is None:
      raise ValueError("All children nodes must have a value")
    
    if not self.children:
      raise ValueError("All children nodes have cannot be empty")
    
    # Create a list to call recursively
    children_html = []
    # Loops through our 'children' to make nesting easier to get through
    for node in self.children:
      # Our recursive call inside of the appended list
      children_html.append(node.to_html())
    return f"<{self.tag}{self.props_to_html()}{''.join(children_html)}></{self.tag}>"