#Write a Python program to find the second smallest number in a list. 
list = [5, 2, 8, 1, 3, 7, 4, 6]

if len(list) < 2:
    print("List should have two numbers.")
else:
    smallest = sec_smallest = float('inf')

    for num in list:
        if num < smallest:
            sec_smallest = smallest
            smallest = num
        elif smallest < num < sec_smallest:
            sec_smallest = num

    print("List of Numbers:", list)
    print("Second Smallest Number:", sec_smallest)