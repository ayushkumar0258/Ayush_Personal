########### Object Oriented Python ############
class Dog:
    def __init__(self, name, age):  ###### Here __init__ is a constructor which is called when an object of the class is created. It initializes the attributes of the class.   and self is a reference to the current instance of the class. It is used to access variables that belong to the class. name and age are attributes of the class which are initialized using the constructor.
        self.name = name #### Here we are assigning the value of name to the instance variable self.name and the value of age to self.age. This allows us to access these attributes using the object of the class.
        self.age = age ##### The __init__ method is a special method in Python classes. It is called when an object of the class is created and is used to initialize the attributes of the class. The self parameter is a reference to the current instance of the class and is used to access the attributes and methods of the class. In this example, we are initializing the name and age attributes of the Dog class using the __init__ method.

    def bark(self):     ##### Here we are defining a method called bark which is a behavior of the Dog class. This method will return the string "Woof!" when called. Methods are functions that are defined inside a class and can be called on objects of that class. In this case, the bark method is a behavior of the Dog class that allows
        return "Woof!"  
my_dog = Dog("Buddy", 5)
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())    

############### what is class and object in python ############
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"  
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_info())

############### Instance Variables and Methods in Python ############
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1 = Person("Alice", 30)
print(person1.greet())  

################# difference of object and instance in python ##############
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some sound"
animal1 = Animal("Dog")
print(animal1.species)
print(animal1.make_sound())     

########### Terminaology of method in python ############
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))  

############### constructor in python ############
class Person:
    def __init__(self, name, age): ####### here __init__ is a constructor which is called when an object of the class is created. It initializes the attributes of the class.   and self is a reference to the current instance of the class. It is used to access variables that belong to the class. name and age are attributes of the class which are initialized using the constructor.
        self.name = name
        self.age = age
person1 = Person("Alice", 30)
print(person1.name)
print(person1.age)      
