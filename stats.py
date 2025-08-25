def count_words(text_data):
    return len(text_data.split())

def count_characters(text_data):
    char_dict = {}
    for char in text_data:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

