from textnode import *
print("hello world")

def main():
    url = TextType.LINK
    example = TextNode("Here is some text", url, "https://www.boot.dev")
    print(example)

if __name__ == "__main__":
    main()