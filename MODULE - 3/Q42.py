#Write a Python program to print all unique values in a dictionary. 
dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}

uni_val = set(dict.values())

print("Unique Values:", uni_val)