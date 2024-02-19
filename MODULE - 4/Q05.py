#Write a Python program to read last n lines of a file. 
file_path = 'C:\\Users\\SMART\\Downloads\\SampleTextFile_20kb.txt'  

n = 1

with open(file_path, 'r') as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]

print(f"Last {n} Lines:")
for line in last_n_lines:
    print(line.strip())