#Write a Python program to unzip a list of tuples into individual lists
tuples = [(1, 'apple'), (2, 'banana'), (3, 'orange')]

lists = list(zip(*tuples))

print("Unzipped Lists:", lists)