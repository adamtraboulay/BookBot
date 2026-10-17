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

def sort_on(count: tuple[str, int]) -> int:
    return count[1]

def chars_dict_to_sorted_list(char_dict):
    char_counts = []
    for char, count in char_dict.items():
        char_counts.append((char, count))
    sorted_chars = sorted(char_counts, reverse=True, key=sort_on)
    return sorted_chars
