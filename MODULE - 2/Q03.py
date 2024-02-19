# Write a Python program to get the Fibonacci series of given range.
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

a, b = 0, 1
fibonacci_series = []

while a <= end:
    if a >= start:
        fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci series within the given range:", fibonacci_series)