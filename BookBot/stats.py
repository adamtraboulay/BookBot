def get_num_words(booktext):
    num_words = len(booktext.split())
    return num_words

def convert_to_lowercase(booktext):
    char_dict = {}
    for char in booktext:

        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
