import sys
from stats import get_num_words
from stats import count_characters
from stats import list_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():    
    text = get_book_text(filepath)
    number_of_words = get_num_words(text)
    characters = count_characters(text)
    char_list = list_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()