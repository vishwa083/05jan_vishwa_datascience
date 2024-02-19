#Write a Python program to check whether a list contains a sub list 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [3, 4, 5]

str1 = ''.join(map(str, list1))
str2 = ''.join(map(str, list2))

if str2 in str1:
    print("it contains the sub-list.")
else:
    print("it does'nt contain the sub-list.")