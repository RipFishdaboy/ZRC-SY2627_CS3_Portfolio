# Single Inheritance

class Parent:
    def func1(self):
        print("Jojo, Lisalisa is your mother.")

class Child(Parent):
    def func2(self):
        print("WHATT.")

obj = Child()
obj.func1()
obj.func2()

# Multiple Inheritance

class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "George Joestar II"
s1.mothername = "Elizabeth Joestar"
s1.parents()

# Multilevel Inheritance

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

s1 = Son('Joseph Joestar', 'George Joestar II', 'Jonathan Joestar')
print(s1.grandfathername)
s1.print_name()

# Hierarchical Inheritance

class Parent:
    def func1(self):
        print("Joseph Joestar")

class Child1(Parent):
    def func2(self):
        print("I'm Joseph's and Erina's daughter, Holly Kujo")

class Child2(Parent):
    def func3(self):
        print("I'm also Joseph's son but my mother is Tomoko, I'm Josuke Higashikata")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()