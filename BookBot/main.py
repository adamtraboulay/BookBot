with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def get_book_text():
    return file_contents

def main():
    booktext = get_book_text()
    print(booktext)

main()
