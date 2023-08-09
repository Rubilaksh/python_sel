#parent class or super class
class Animal:
    animalName=""
    def eat(self):
        print("Animal will eat")

#child class or sub class
class Dog(Animal):

    def bark(self):
        print("Dog will bark")
        print("The animal name is ",self.animalName)

d= Dog()
d.animalName="dog"
d.bark()
d.eat()

