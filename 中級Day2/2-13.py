class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self,keisyo):
        return f"Hello! I'm {self.name}{keisyo}."
   
p1 = Person('Bob', 25)
print(p1.greet("様"))

p2 = Person('Tom', 32)
print(p2.greet("様"))
