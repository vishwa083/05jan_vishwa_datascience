#Write a Python script to check if a given key already exists in a dictionary. 
dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

key = 'orange'

if key in dict:
    print(f"key '{key}' exists")
else:
    print(f"key '{key}' does not exist")