from textnode import *

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
        simple_tags = ["b", "p", "i", "ul", "li", "ol", "blockquote", "code",
                        "h1", "h2", "h3", "h4", "h5", "h6", "div", "span"]
        if self.value == None:
            raise ValueError("Leaf Node is missing a value.")
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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent Node must have a tag.")
        
        if self.children == None or self.children == []:
            raise ValueError("Parent Node must have children.")
        
        final_html_string = ""

        if len(self.children) < 1:
                return final_html_string
        
        for child in self.children: 
            result = child.to_html()
            final_html_string = final_html_string + result

        return f"<{self.tag}>{final_html_string}</{self.tag}>"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception(f"Invalid TextType: {text_node.text_type}")