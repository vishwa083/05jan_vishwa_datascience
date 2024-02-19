#Write a Python function that takes two lists and returns true if they have at least one common member.
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

set_a = set(list_a)
set_b = set(list_b)

if set_a.intersection(set_b):
    print("have one common member.")
else:
    print("don't have any common members.")