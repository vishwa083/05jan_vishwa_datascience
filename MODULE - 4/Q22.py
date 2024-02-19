#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 
"Class: Blueprint for creating objects, defining attributes and behaviors."
"Self: The self parameter is a reference to the instance of the class and is used to access its attributes and methods."

class Dog:
    pass  

my_dog = Dog()
my_dog.name = "Buddy"
my_dog.age = 3

print(f"{my_dog.name} is {my_dog.age} years old.")