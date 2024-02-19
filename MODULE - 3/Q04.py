#Write a Python function to get the largest number, smallest num and sum of all from a list.
my_list = [2, 33, 222, 14, 25]
if not my_list:
    print("list is empty")
else:
    largest = smallest = total_sum = my_list[0]
    for num in my_list[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        total_sum += num
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Sum:", total_sum)