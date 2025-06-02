from stats import get_word_count, get_book_text, get_character_count, sort_character_list
import sys

try:
    book_path = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(book_path))} total words")
    print("--------- Character Count -------")

    for char, count in (sort_character_list(get_character_count(get_book_text(book_path)))):
        if char.isalpha() == True:
            print(f"{char}: {count}")

    print("============= END ===============")

main()
