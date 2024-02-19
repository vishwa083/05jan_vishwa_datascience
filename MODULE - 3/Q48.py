#Write a Python function to calculate the factorial of a number (a nonnegative integer) 
num = 5

fac = 1
for i in range(1, num + 1):
    fac *= i

print(f"The factorial of {num} is: {fac}")