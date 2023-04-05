# 演習２－04
# あるリストについて、その含まれる要素のidとtypeのリストを要素とする二次元リストを生成する式を、リスト内包表記をつかって作成しましょう。

# copilotが書いたコード
# def main():
#     x = [10]
#     print(x[0], id(x), type(x))
    
#     x[0] += 1
#     print(x[0], id(x), type(x))
    
#     y = [10]
#     print(y[0], id(y), type(y))
    
#     y[0] += 1
#     print(y[0], id(y), type(y))
    
#     z = [x, y]
#     print(z)
    
#     print([[id(z[i][0]), type(z[i][0])] for i in range(len(z))])

# if __name__ == '__main__':
#     main()

# ChatGPTが書いたコード
def generate_id_type_list(input_list):
    """
    与えられたオブジェクトのリストから、id と type の値を含む 2 次元リストを生成します。

    引数:
        input_list (list): id と type の属性を持つオブジェクトのリスト

    戻り値:
        list: id と type の値を含む 2 次元リスト
    """
    result = [[id(item), type(item)] for item in input_list]
    return result

class Item:
    def __init__(self, id, type):
        self.id = id
        self.type = type

def main():
    input_list = [Item(1, 'A'), Item(2, 'B'), Item(3, 'C')]
    id_type_list = generate_id_type_list(input_list)
    print(id_type_list)

if __name__ == "__main__":
    main()