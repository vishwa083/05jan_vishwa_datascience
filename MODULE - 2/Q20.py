#Write a Python function that takes a list of words and returns the length of the longest one.
words_list = input("Enter a list of words separated by space: ").split()
max_length = 0

for word in words_list:
    if len(word) > max_length:
        max_length = len(word)

print("Length of the longest word:", max_length)

