#Write a Python program to count the number of characters (character frequency) in a string.
string = input("Enter a string: ")

unique_chars = []

for char in string:
    if char not in unique_chars:
        unique_chars.append(char)  
        count = string.count(char)  
        print(f"Character '{char}' appears {count} times in the string.")
