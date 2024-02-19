#Write python program that swap two number with temp variable and without temp variable.
#Swapping with a temporary variable:
'''num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Before swapping: num1 =", int(num1), "num2 =", int(num2))

temp = num1
num1 = num2
num2 = temp

print("After swapping: num1 =", int(num1), "num2 =", int(num2))'''

# Swapping without a temporary variable
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Before swapping: num1 =", int(num1), "num2 =", int(num2))

num1,num2=num2,num1

print("After swapping: num1 =", int(num1), "num2 =", int(num2))

