from stats import get_word_count, get_book_text, get_character_count
book_path = "books/frankenstein.txt"

def main():    

    print(f"{get_word_count(get_book_text(book_path))} words found in the document")
    print(get_character_count(get_book_text(book_path)))
    
main()
