#Write a Python program to read first n lines of a file. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

n = 1

with open(file_path, 'r') as file:
    first = [next(file) for _ in range(n)]

print(f"First {n} Lines:")
for line in first:
    print(line.strip())