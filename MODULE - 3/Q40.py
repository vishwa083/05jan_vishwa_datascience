#Write a Python program to map two lists into a dictionary 
keys = ['apple', 'banana', 'orange']
values = [5, 3, 7]

mapped = dict(zip(keys, values))

print("Mapped Dictionary:", mapped)