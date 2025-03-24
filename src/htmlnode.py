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
      attributes = [f' {key}="{value}' for key, value in self.props.items()]
      
      # Join the list into a single string and return it
      return "".join(attributes)
    
    def __repr__(self):
      pass