#Write a Python program to remove an empty tuple(s) from a list of tuples. 
tuple = (1, 2, (), 3, 2, 4, (), 5, 2, 6, 2)
list = [t for t in tuple if t]

print("Tuples without Empty Tuples:", list)