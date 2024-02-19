#Write a Python program to copy the contents of a file to another file. 
file1 = 'C:\\Users\\SMART\\Downloads\\source-release.txt'  
file2 = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

with open(file1, 'r') as source_file:
    content = source_file.read()

with open(file2, 'w') as destination_file:
    destination_file.write(content)

print(f"Contents copied from '{file1}' to '{file2}'.")