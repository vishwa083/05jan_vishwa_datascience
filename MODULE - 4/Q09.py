#Write a Python program to count the number of lines in a text file. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

with open(file_path, 'r') as file:
    num = sum(1 for line in file)

print(f"The number of lines in the file is: {num}")