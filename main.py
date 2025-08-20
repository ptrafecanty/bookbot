from stats import sys, get_book_text, word_counter, character_counter, sort_on, sorted_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    #contents = get_book_text(f"books/frankenstein.txt")
    contents = get_book_text(filename)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    #print(contents)
    print(word_counter(contents))
    print("--------- Character Count -------")
    characters_counted = (character_counter(contents))
    sorted_list = sorted_characters(characters_counted)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()