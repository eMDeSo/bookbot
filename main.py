import sys
from stats import count_words, count_characters, dict_to_list

def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        book_text = get_books_text(filepath)
        words_count = count_words(book_text)
        char_dict = count_characters(book_text)
        sorted_char_list = dict_to_list(char_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        for item in sorted_char_list:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
