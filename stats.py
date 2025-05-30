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

def get_character_count(book_text):
    raw_text = book_text.lower()
    character_dict = {}

    for char in raw_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict


