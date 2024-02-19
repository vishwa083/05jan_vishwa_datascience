#Write a Python function to insert a string in the middle of a string.
# Input the original string and the string to insert from the user
original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

middle_index = len(original_string) // 2

result_string = original_string[:middle_index] + string_to_insert + original_string[middle_index:]

print("Resulting string:", result_string)
