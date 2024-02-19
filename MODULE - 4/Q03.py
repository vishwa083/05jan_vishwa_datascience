#Write a Python program to append text to a file and display the text.
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'

text = "This is new text to append to the file.\n"

with open(file_path, 'a') as file:
    file.write(text)

with open(file_path, 'r') as file:
    new = file.read()

print("Updated File Content:")
print(new)