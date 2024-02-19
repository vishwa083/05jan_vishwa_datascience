#Write a Python function to check whether a number is in a given range
# Example usage without a function
num = 4
range1 = 5
range2 = 10

if range1 <= num <= range2:
    print(f"{num} is in the range [{range1}, {range2}]")
else:
    print(f"{num} is NOT in the range [{range1}, {range2}]")