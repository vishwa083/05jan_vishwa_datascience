#Write a Python script to concatenate following dictionaries to create a new one. 
dict1 = {'apple': 5, 'banana': 3}
dict2 = {'orange': 7, 'grape': 2}
dict3 = {'kiwi': 4, 'melon': 6}

concat_dict1 = dict1.copy()
concat_dict1.update(dict2)
concat_dict1.update(dict3)

concat_dict2 = {**dict1, **dict2, **dict3}

print("Original Dictionaries:")
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)

print("\nConcatenated Dictionary (Method 1):", concat_dict1)
print("Concatenated Dictionary (Method 2):", concat_dict2)