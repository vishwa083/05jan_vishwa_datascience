#Write a Python program to find the highest 3 values in a dictionary 
dict = {'a': 10, 'b': 25, 'c': 15, 'd': 30, 'e': 20}

sort = sorted(dict.values(), reverse=True)
values = sort[:3]

print("Highest 3 Values:", values)