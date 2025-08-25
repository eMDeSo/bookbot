from stats import count_words, count_characters, dict_to_list

def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_books_text(filepath)
    words_count = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_char_list = dict_to_list(char_dict)
    #print(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
