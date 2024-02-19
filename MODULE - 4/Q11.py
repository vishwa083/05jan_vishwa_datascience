#Write a Python program to write a list to a file.
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

list = ['apple', 'banana', 'orange', 'grape']

with open(file_path, 'w') as file:
    for item in list:
        file.write(f"{item}\n")

print(f"The list has been written to the file: {file_path}")