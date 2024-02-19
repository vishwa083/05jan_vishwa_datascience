#Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

swapped_string1 = string2[:2] + string1[2:]
swapped_string2 = string1[:2] + string2[2:]

result_string = swapped_string1 + ' ' + swapped_string2

print("Result string with swapped first two characters:")
print(result_string)

