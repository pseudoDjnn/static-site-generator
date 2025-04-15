from textnode import TextNode, TextType

def extract_title(markdown):
    pass

def main():
    #  Create a test TextNode ( for example, a link)
    node = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    #  Print the node to see its string representation
    print(node)

if __name__=="__main__":
    main()
