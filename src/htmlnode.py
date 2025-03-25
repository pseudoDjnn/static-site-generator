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
  def __init__(self, tag, value):
    super().__init__(tag, value=value, children=None)
    if not value:
      raise ValueError("All leaf nodes must have a value")
    
    
  def to_html(self):
    if not self.value:
      raise ValueError("All leaf nodes must have a value")
    
    if not self.tag:
      return self.value