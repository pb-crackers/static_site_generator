import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_eq_more(self):
        node = TextNode("My Text", TextType.TEXT, url="www.test.com")
        node2 = TextNode("My Text", TextType.TEXT, url="www.test.com")
        self.assertEqual(node, node2)
    
    def test_more_not_eq(self):
        node = TextNode("This is my text", TextType.CODE)
        node2 = TextNode("More text here", TextType.BOLD, url="www.urls.com")
        self.assertNotEqual(node, node2)

    def test_more_not_eq(self):
        node = TextNode("More text here", TextType.BOLD)
        node2 = TextNode("More text here", TextType.BOLD, url="www.urls.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()