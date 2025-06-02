from stats import get_word_count, get_book_text, get_character_count, sort_character_list
book_path = "books/frankenstein.txt"

def main():    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(book_path))} total words")
    print("--------- Character Count -------")

    for char, count in (sort_character_list(get_character_count(get_book_text(book_path)))):
        if char.isalpha() == True:
            print(f"{char}: {count}")
    #print(sort_character_list(get_character_count(get_book_text(book_path))))
    print("============= END ===============")
main()
