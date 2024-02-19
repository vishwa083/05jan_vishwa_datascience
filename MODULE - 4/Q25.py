##Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 
class Circle:
    def __init__(self, radius):
        self.radius = radius

circle = Circle(radius=4)

print(f"Radius: {circle.radius}")
print(f"Area: {3.14 * circle.radius**2}")
print(f"Perimeter: {2 * 3.14 * circle.radius}")