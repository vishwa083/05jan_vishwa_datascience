#Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

des = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order:", asc)
print("Descending Order:", des)