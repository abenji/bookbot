book_path = "books/frankenstein.txt"

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def main():
    print(get_book_text(book_path))

main()
