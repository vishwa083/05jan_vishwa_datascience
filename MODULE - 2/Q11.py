#Write a python program to sum of the first n positive integers.
n = int(input("Enter a positive integer n: "))

sum_of_integers = (n * (n + 1)) // 2

print("The sum of the first", n, "positive integers is:", sum_of_integers)
