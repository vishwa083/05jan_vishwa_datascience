#Write a Python program to read a file line by line store it into a variable. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'   

with open(file_path, 'r') as file:
    file = file.read()

print("Content stored:")
print(file)