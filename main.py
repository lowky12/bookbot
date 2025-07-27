import sys
from stats import get_num_words, get_num_chars, sort_char_dict

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book = get_book_text(path)
    num_words = get_num_words(book)
    
    chars = get_num_chars(book)
    sort_char_list = sort_char_dict(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for i in sort_char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



if __name__ == "__main__":
    main()