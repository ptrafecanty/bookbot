def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
    words = file_contents.split()
    num_words = len(words)
    number_words = f"{num_words} words found in the document"
    return number_words

def character_counter(file_contents):
    lowercase_contents = file_contents.lower()
    lowercase_dict = {}
    for letter in lowercase_contents:
        if letter in lowercase_dict:
            lowercase_dict[letter] += 1
        else:
            lowercase_dict[letter] = 1
    return lowercase_dict
