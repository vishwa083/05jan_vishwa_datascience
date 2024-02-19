#Write a Python program to convert a tuple to a string. 
tuple = (1, 'Hello', 3.14, True)
string = ''.join(map(str, tuple))

print("Original Tuple:", tuple)
print("String:", string)