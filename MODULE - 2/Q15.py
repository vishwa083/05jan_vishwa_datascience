#Write a Python program to count occurrences of a substring in a string.
string = input("Enter a string: ")
substring = input("Enter a substring to count: ")

count = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        count += 1

print(f"The substring '{substring}' appears {count} times in the string.")