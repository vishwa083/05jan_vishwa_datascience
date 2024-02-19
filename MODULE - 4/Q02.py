#Write a Python program to read an entire text file. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

    print("File Content:")
    print(file_content)