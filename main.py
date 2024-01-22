import os

directory = input("please enter directory: ")

try:
    with open(directory, 'r') as file:
        passage = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()
word = input("\nword: ")
space = " "
full_word = space + word + space

def count_word_line(line, full_word):

    line_lower = line.lower()

    word_lower = full_word.lower()

    occurrences = line_lower.count(word_lower)

    return occurrences

for i, line in enumerate(passage, start=1):
    occurrences_in_line = count_word_line(line, full_word)
    if occurrences_in_line >= 1:
        print(f"Line {i}: The word '{word}' appears {occurrences_in_line} times.")