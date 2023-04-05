# 演習２－17

# クラスOnigiriに__str__メソッドを追加しましょう。

class Onigiri:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'name: {self.name} price: {self.price} stock: {self.stock}'
    
    def get_tax_included(self, tax_rate=0.1):
        return int(self.price * (1 + tax_rate))
    
    def is_sold_out(self):
        return self.stock == 0

def main():
    o1 = Onigiri('たまご', 100, 10)
    print(o1)

    o2 = Onigiri('えび', 120, 20)
    print(o2)

if __name__ == '__main__':
    main()

