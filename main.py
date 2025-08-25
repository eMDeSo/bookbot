def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    print(get_books_text("./books/frankenstein.txt"))

main()
