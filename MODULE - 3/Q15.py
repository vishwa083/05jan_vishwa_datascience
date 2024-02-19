#Write a Python program to get unique values from a list 
list1 = [1, 2, 3, 1, 2, 4, 5, 6, 4]

list2 = list(set(list1))

print("Original List:", list1)
print("Unique Values:", list2)