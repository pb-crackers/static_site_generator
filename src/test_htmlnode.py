import unittest

from textnode import *
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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_parent_no_tag(self):
        parent_node = ParentNode(None, ["node"])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children_empty_array(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_text_to_html_type_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_type_italic(self):
        node = TextNode("My text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "My text")

    def test_text_to_html_type_link(self):
        node = TextNode("My text", TextType.LINK, "www.mylink.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "My text")
        self.assertEqual(html_node.props, {"href":"www.mylink.com"})

    def test_text_to_html_type_img(self):
        node = TextNode("My text", TextType.IMAGE, "www.mylink.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"www.mylink.com", "alt": "My text"})


if __name__ == "__main__":
    unittest.main()