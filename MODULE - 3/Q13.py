#Write a Python program to select an item randomly from a list. 
import random

my_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']

if my_list:
    random_item = random.choice(my_list)
    print("List of Items:", my_list)
    print("Randomly Selected Item:", random_item)
else:
    print("List is empty.")