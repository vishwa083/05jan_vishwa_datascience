#Differentiate between append () and extend () methods? 
"The append() method is used to add a single element to the end of a list."
list = [1, 2, 3]
list.append(4)
print(list)

"The extend() method is used to add elements from an iterable (such as a list, tuple, or another iterable) to the end of a list."
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

"append() adds a single element at the end of the list, while extend() adds elements from an iterable to the end of the list"