class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def greet(self):
        print(f"Hello! I'm {self.name}.")

p1 = Person('Bob', 25)
print(p1.name, p1.age)
p1.greet()

p2 = Person('Tom', 32)
print(p2.name, p2.age)
p2.greet()
