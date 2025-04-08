import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("p", "this is text of the paragraph", [], 
        {"href": "https://www.google.com",
        "target": "_blank",
        }
        )
        conversion = node1.props_to_html()
        answer = 'href=https://www.google.com target=_blank'
        self.assertEqual(conversion, answer)

    def repeating_the_above_test(self):
        node = HTMLNode("h1", "this is text of the paragraph", [], 
        {"href": "https://www.google.com",
        "target": "_blank",
        })
        conversion = node.props_to_html()
        answer = 'href=https://www.google.com target=_blank'
        self.assertEqual(conversion, answer)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href="'https://www.google.com'">Click me!</a>")

    def test_leaf_to_html_img(self):
        node = LeafNode(tag="img", value = "", props={"src": "url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.to_html(), "<img src="'url/of/image.jpg'" alt="'Description of image'" />")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is my paragraph")
        self.assertEqual(node.to_html(), "<h1>This is my paragraph</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is my paragraph")
        self.assertEqual(node.to_html(), "This is my paragraph")

if __name__ == "__main__":
    unittest.main()