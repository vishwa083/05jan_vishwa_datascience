#Write a Python function that takes a list and returns a new list with unique elements of the first list. 
list1 = [1, 2, 3, 1, 2, 4, 5, 6, 4]

list2 = list(set(list1))

print("Original List:", list1)
print("Unique Elements:", list2)