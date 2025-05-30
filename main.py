def main():
    book_path = "books/frankenstein.txt"

    def get_book_text(book_path):
        book_text = ""
        with open(book_path) as f:
            book_text = f.read()
            return book_text
        
    def get_word_count(book_text):
        word_count = 0
        words = book_text.split()
        word_count = len(words)
        return word_count
    
    print(f"{get_word_count(get_book_text(book_path))} words found in the document")

main()
