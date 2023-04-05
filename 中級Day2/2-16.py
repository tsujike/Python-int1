class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name} age: {self.age}'
   
p1 = Person('Bob', 25)
print(p1)

p2 = Person('Tom', 32)
print(p2)
