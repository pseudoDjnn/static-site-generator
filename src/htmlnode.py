class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props
      
    def to_html(self):
      raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
      if self.props is None:  #  Check for None or empty dictionary
        return ""
      
      props_html = ""
      for prop in self.props:
        props_html += f' {prop}="{self.props[prop]}"'
      return props_html
    
    def __repr__(self):
      return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
      
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
  
  def __repr__(self):
    return f"LeadNode({self.tag}, {self.value}, {self.props})"
  
  
class ParentNode(HTMLNode):
  # Make tag and children mandatory and props optional
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
    
  # First recursive call
  def to_html(self):
    # Check to see it meets our requirements 
    if self.tag is None:
      raise ValueError("Invalid HTML: no tag")
    if self.children is None:
      raise ValueError("Invalid HTML: no children")
    
    # Create a list to call recursively
    children_html = ''
    # Loops through our 'children' to make nesting easier to get through
    for child in self.children:
      # Our recursive call
      children_html += child.to_html()
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
  
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"