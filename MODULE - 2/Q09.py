#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Sum will be zero because two or more values are equal.")
    sum = 0
else:
    sum = num1 + num2 + num3

print("Sum of the three integers:", sum)
