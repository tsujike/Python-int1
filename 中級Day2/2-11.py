# 演習２－11

# クラスPersonに以下のインスタンス変数を追加で定義してください。
# 身長を表すプロパティ: height
# 体重を表すプロパティ: weight

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

def main():
    p1 = Person('Bob', 25, 170, 60)
    print(p1.name, p1.age, p1.height, p1.weight)

    p2 = Person('Tom', 32, 180, 70)
    print(p2.name, p2.age, p2.height, p2.weight)

if __name__ == '__main__':
    main()
    