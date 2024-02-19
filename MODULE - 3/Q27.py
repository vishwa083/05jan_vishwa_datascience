#Write a Python program to find the repeated items of a tuple.
tuple = (1, 2, 3, 2, 4, 5, 2, 6, 2)

items = {item for item in tuple if tuple.count(item) > 1}

print("Repeated Items:", items)