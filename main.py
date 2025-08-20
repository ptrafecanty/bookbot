from stats import get_book_text, word_counter, character_counter

def main():
    contents = get_book_text(f"books/frankenstein.txt")
    print(contents)
    print(word_counter(contents))
    print(character_counter(contents))
main()