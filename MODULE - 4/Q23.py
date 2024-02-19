#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

rectangle = Rectangle(length=5, width=3)

print(f"Length: {rectangle.length}")
print(f"Width: {rectangle.width}")
print(f"Area: {rectangle.length * rectangle.width}")