class HTMLNode():
    def __init__(self, 
                tag: str = None, 
                value: str = None, 
                children: list = None, 
                props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        final_string = ""
        if self.props != None:
            for key in self.props:
                final_string = final_string + f'{key}={self.props[key]} ' 
            return final_string.strip()
        else:
            raise Exception("self.props cannot be None")
    
    def __repr__(self):
        return f"HTML Node: {self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        simple_tags = ["b", "p", "i", "ul", "li", "ol", "blockquote", "code", "h1", "h2", "h3", "h4", "h5", "h6"]
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            if self.tag in simple_tags:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
            elif self.tag == "a":
                html_props = self.props_to_html()
                return f"<a {html_props}>{self.value}</a>"
            
            elif self.tag == "img":
                props = self.props_to_html()
                return f"<img {props} />"
            
            else:
                raise Exception("That tag wasn't account for in your LeafNode Class.")
