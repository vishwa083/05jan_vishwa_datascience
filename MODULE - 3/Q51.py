#Write a Python function that checks whether a passed string is palindrome or not
str1 = "kashish lalakiya"

str2 = ''.join(str1.lower().split())

if str2 == str2[::-1]:
    print(f"The string '{str1}' is a palindrome.")
else:
    print(f"The string '{str1}' is NOT a palindrome.")