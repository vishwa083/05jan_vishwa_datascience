#Write a Python program to convert a list of tuples into a dictionary.
tuples = [('apple', 1), ('banana', 2), ('orange', 3)]

result_dict = {key: value for key, value in tuples}

print("Dictionary:", result_dict)