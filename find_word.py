import os
import re
from contextlib import redirect_stdout

os.path.expanduser("/article2.txt")

def count_word_line(line, word):
    pattern = re.compile(rf'\b{re.escape(word)}\b', flags=re.IGNORECASE)
    occurrences = len(pattern.findall(line))
    return occurrences

def find_and_print_occurrences(full_passage, word):
    word_found = False
    for i, line in enumerate(full_passage, start=1):
        occurrences_in_line = count_word_line(line, word)
        if occurrences_in_line >= 1:
            print(f"Line {i}: The word '{word}' appears {occurrences_in_line} times.")
            word_found = True
    if not word_found:
        print(f"The word '{word}' is not found in the passage.")

def replace_words_in_passage(full_passage, word, replace_word):
    new = re.sub(rf'\b{re.escape(word)}\b', replace_word, full_passage, flags=re.IGNORECASE)
    print(new)


while True:
    path = input("Please enter the full path of the file: ")

    try:
        with open(path, 'r') as file:
            passage = file.readlines()
            file.seek(0)
            full_passage= file.read()
        break  # Exit the loop if the file is successfully opened
    except FileNotFoundError:
        print(f"Error: File '{path}' not found. Please re-enter the file path.")


word = input("\nword: ")
replace_word = input("\nWhat word would you like to replace it with? ")

with open('article2.txt', 'w') as f:
    with redirect_stdout(f):
        replace_words_in_passage(full_passage, word, replace_word)
        find_and_print_occurrences(passage, word)
