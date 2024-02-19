#Write a Python program to read a file line by line and store it into a list
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

with open(file_path, 'r') as file:
    list = file.readlines()

print("Lines stored in the list:")
for line in list:
    print(line.strip())