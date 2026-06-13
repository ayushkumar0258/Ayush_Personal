class Animal:
    def __init__(self,species):
        self.species=species
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def __init__(self,name,bread):
        self.name=name
        self.bread=bread
        super().__init__('Dog')
dog=Dog('Moti','Good')
print(dog.name)
print(dog.make_sound())    
print(dog.species)
