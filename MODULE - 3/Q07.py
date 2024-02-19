#Write a Python program to remove duplicates from a list. 
list1 = [1, 2, 3, 1, 2, 4, 5, 6, 4]

list2 = list(set(list1))

print("Original List:", list1)
print("Duplicates:", list2)