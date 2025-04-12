from htmlnode import *
from textnode import *
import re

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
    
def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        if node.text_type == TextType.TEXT:
            try:
                split_strings = node.text.split(delimiter)
                new_nodes.append(TextNode(split_strings[0], TextType.TEXT))
                new_nodes.append(TextNode(split_strings[1], text_type))
                new_nodes.append(TextNode(split_strings[2], TextType.TEXT))
            except Exception:
                raise Exception(f"No closing delimiter {delimiter}")
        else:
            new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    # takes a string, returns tuple: (alt text, url)
    try:
        matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matches
    except Exception:
        return "The markdown provided is not valid. There may be nested brackets."

def extract_markdown_links(text):
    # takes a string, returns tuple: (hyperlink text, url)
    try:
        matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matches
    except Exception:
        return "The markdown provided is not valid. There may be nested brackets."
