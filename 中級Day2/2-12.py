# 演習2－12

# 以下のインスタンス変数を持つクラスOnigiriと、いくつかのインスタンスを作成してください。
# 商品名（＝おにぎりの具）を表すプロパティ: name
# 販売金額を表すプロパティ: price
# 在庫数を表すプロパティ: stock

class Onigiri:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

def main():
    o1 = Onigiri('たまご', 100, 10)
    print(o1.name, o1.price, o1.stock)

    o2 = Onigiri('えび', 120, 20)
    print(o2.name, o2.price, o2.stock)

if __name__ == '__main__':
    main()

