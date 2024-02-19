#Write a Python program to check whether an element exists within a tuple. 
tuple = (1, 'apple', 3.14, True)

element = 'apple'

if element in tuple:
    print(f"element '{element}' exists")
else:
    print(f"element '{element}' does not exist")