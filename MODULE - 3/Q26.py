#Write a Python program to replace last value of tuples in a list. 
tuples = [(1, 2, 3), ('apple', 'banana', 'orange'), (3.14, 2.71, 1.61)]

value = 'new_value'

modified = [(t[:-1] + (value,)) for t in tuples]

print("Modified List:", modified)