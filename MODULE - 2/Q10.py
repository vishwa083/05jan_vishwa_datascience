#Write a Python program that will return true if the two given integer 
#values are equal or their sum or difference is 5.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 == num2 or abs(num1 - num2) == 5 or num1 + num2 == 5:
    result = True
else:
    result = False

print("Result:", result)
