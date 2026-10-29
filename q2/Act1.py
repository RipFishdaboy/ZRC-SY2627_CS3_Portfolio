class Animal:
    def __init__(self, name):
        self.__name = name

    def make_sound(self):
        print(self.__name, "makes a sound.")

    def eat (self):
        print(self.__name, "is eating.")

class Lion(Animal):
    def make_sound(self):
        print(self.__name, "roars loudly!")

    def eat(self):
        print(self.__name, "eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(self.__name, "trumpets!")

    def eat(self):
        print(self.__name, "eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(self.__name, "chatters!")

    def eat(self):
        print(self.__name, "eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound()) 
print(elephant.eat())   
print("-----")

print(monkey.make_sound())  
print(monkey.eat())   
print("-----")