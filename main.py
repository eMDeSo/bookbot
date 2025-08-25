from stats import count_words, count_characters

def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_text = get_books_text("./books/frankenstein.txt")
    print(f"{count_words(book_text)} words found in the document")
    print(count_characters(book_text))


main()
