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

def sort_on(items):
    return items["num"]

def dict_to_list(dictionary):
    list_of_dictionaries = []
    for key, value in dictionary.items():
        if key.isalpha():
            list_of_dictionaries.append({"char": key, "num": value})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

