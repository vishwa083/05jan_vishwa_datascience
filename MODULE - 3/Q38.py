#Write a Python program to check multiple keys exists in a dictionary
dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

keys = ['apple', 'banana', 'kiwi']

if all(key in dict for key in keys):
    print("All keys exist")
else:
    print("one key does not exist")