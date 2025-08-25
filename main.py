def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(text_data):
    counter = 0
    for word in (text_data.split()):
        counter += 1
    return counter

def main():
    #print(get_books_text("./books/frankenstein.txt"))
    print(f"{count_words(get_books_text("./books/frankenstein.txt"))} words found in the document")



main()
