#How will you set the starting value in generating random numbers?
import random

start = 42
random.seed(start)

num1 = random.random()
num2 = random.randint(1, 10)

print("Random number 1:", num1)
print("Random number 2:", num2)