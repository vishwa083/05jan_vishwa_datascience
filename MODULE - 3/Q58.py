#Write a Python program to read a random line from a file. 
import random
import linecache

name = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'
with open(name, 'r') as file:
    lines = sum(1 for line in file if line.strip())

if lines == 0:
    print("No non-empty lines in the file.")
else:
    num = random.randint(1, lines)

    with open(name, 'r') as file:
        for _ in range(num):
            line = file.readline().strip()
            while not line:
                line = file.readline().strip()

    print("Random Line:", line)