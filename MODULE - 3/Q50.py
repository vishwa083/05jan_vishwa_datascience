#Write a Python function to check whether a number is perfect or not.
num = 28

if num <= 0:
    print(f"{num} is NOT a perfect number.")
else:
    sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum += divisor

    if sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is NOT a perfect number.")