#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list = ["aba", "xyz", "abca", "1221", "python"]

count = 0

for string in list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(f"same character: {count}")