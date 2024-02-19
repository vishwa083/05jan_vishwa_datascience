#Write a Python program to count the frequency of words in a file. 
from collections import Counter
import re

file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt' 

with open(file_path, 'r') as file:
    words = re.findall(r'\b\w+\b', file.read().lower())

fre = Counter(words)

print("Word frequencies in the file:")
for word, frequency in fre.items():
    print(f"{word}: {frequency}")