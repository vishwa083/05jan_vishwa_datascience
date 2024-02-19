#Write python program that user to enter only odd numbers, else will raise an exception. 
while True:
    try:
        user = int(input("odd number: "))
        if user % 2 == 0:
            raise ValueError("enter odd number.")
        else:
            print("You entered:", user)
            break
    except ValueError as e:
        print(f"Error: {e}")