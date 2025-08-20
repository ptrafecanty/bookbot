<<<<<<< HEAD
=======
import sys

>>>>>>> 06d28b7 (Added stats)
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
    words = file_contents.split()
    num_words = len(words)
<<<<<<< HEAD
    number_words = f"{num_words} words found in the document"
=======
    number_words = f"Found {num_words} total words"
>>>>>>> 06d28b7 (Added stats)
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
<<<<<<< HEAD
=======

def sort_on(items):
    return items["num"]

def sorted_characters(char_dicts):
    list_of_dicts = []
    for char, count in char_dicts.items():
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
>>>>>>> 06d28b7 (Added stats)
