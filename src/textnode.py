from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        true_meter = 0
        if other.text == self.text:
            true_meter += 1
        if other.text_type.value == self.text_type.value:
            true_meter += 1
        if other.url == self.url:
            true_meter += 1
        
        if true_meter == 3:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"