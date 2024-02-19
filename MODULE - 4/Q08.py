#Write a python program to find the longest words. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

with open(file_path, 'r') as file:
    words = file.read().split()

max = len(max(words, key=len))

word = [word for word in words if len(word) == max]

print(f"The longest word(s) with a length of {max} character(s):")
for word in word:
    print(word)