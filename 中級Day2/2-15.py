# 演習２－15

# クラスOnigiriに税込価格を返すget_tax_includedメソッドと、売り切れかどうかをブール値で返すis_sold_outメソッドを追加してください。
# なお、get_tax_includedメソッドの引数として税率を表す数値を渡すことができるものとし、その省略時は0.1を採用するものとします。

class Onigiri:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def get_tax_included(self, tax_rate=0.1):
        return int(self.price * (1 + tax_rate))
    
    def is_sold_out(self):
        return self.stock == 0

def main():
    o1 = Onigiri('たまご', 100, 10)
    print(o1.name, o1.price, o1.stock)
    print(o1.get_tax_included())
    print(o1.is_sold_out())

    o2 = Onigiri('えび', 120, 20)
    print(o2.name, o2.price, o2.stock)
    print(o2.get_tax_included())
    print(o2.is_sold_out())

if __name__ == '__main__':
    main()