''' Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.
'''
given_string = input("Enter a string: ")

if len(given_string) >= 2:
    result_string = given_string[:2] + given_string[-2:]
else:
    result_string = ""
print("Resulting string:", result_string)
