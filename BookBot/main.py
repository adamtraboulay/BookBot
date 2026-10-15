
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def get_book_text():
    return file_contents

def get_num_words():
    booktext = get_book_text()
    num_words = len(booktext.split())
 
def main():
    booktext = get_book_text()
    num_words = len(booktext.split())
    print(f"Found {num_words} total words")

main()
