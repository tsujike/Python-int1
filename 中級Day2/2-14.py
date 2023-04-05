# 演習２－14

# クラスPersonに、BMIを返すget_bmiメソッドを追加しましょう。
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_bmi(self):
        return self.weight / (self.height / 100) ** 2

def main():
    p1 = Person('Bob', 25, 170, 60)
    print(p1.name, p1.age, p1.height, p1.weight)
    print(p1.get_bmi())

    p2 = Person('Tom', 32, 180, 70)
    print(p2.name, p2.age, p2.height, p2.weight)
    print(p2.get_bmi())

if __name__ == '__main__':
    main()