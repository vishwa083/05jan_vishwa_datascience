#How can you pick a random item from a list or tuple? 
"We can use the random.choice() function from the random module to pick a random item from a list or tuple."

import random

list = [1, 2, 3, 4, 5]
random1 = random.choice(list)
print("Random item from list:", random1)

tuple = ('apple', 'banana', 'orange', 'grape')
random2 = random.choice(tuple)
print("Random item from tuple:", random2)