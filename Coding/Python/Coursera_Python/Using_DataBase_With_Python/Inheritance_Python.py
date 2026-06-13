############# Inheritance in python#############
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some sound" 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")  # Call the constructor of the parent class
        self.name = name
        self.breed = breed

    def make_sound(self):
        return "Woof!"
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  
print(my_dog.breed)
print(my_dog.species)
print(my_dog.make_sound())