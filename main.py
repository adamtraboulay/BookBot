import sys
from stats import get_num_words, convert_to_lowercase, chars_dict_to_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(
    book_path: str, num_words: int, chars_sorted_list: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in chars_sorted_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    booktext = get_book_text(book_path)
    num_words = get_num_words(booktext)
    converted_text = convert_to_lowercase(booktext)
    sorted_chars = chars_dict_to_sorted_list(converted_text)

    print_report(book_path, num_words, sorted_chars)

main()
