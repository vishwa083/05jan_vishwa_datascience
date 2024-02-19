#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 
"Inheritance: Mechanism for a class to inherit properties and behaviors from another."
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, breed):
        super().__init__(species="Dog")
        self.breed = breed

animal = Animal(species="Unknown")
dog = Dog(breed="Golden Retriever")

print(f"Animal Species: {animal.species}")
print("animal sound")

print(f"Dog Species: {dog.species}")
print(f"Dog Breed: {dog.breed}")
print("Woof! Woof!")

"A constructor is a special method named __init__."
"It is automatically called when an object is created from a class."