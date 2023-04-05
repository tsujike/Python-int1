# 公式リファレンス　https://docs.python.org/ja/3/index.html

# global_msg = 'グローバル変数'

# def func():
#     local_msg = 'ローカル変数'
#     print(f'ローカルで{global_msg}')
#     print(f'ローカルで{local_msg}')
# func()

# print(f'グローバルで{global_msg}')
# print(f'グローバルで{local_msg}') #NameErrorになる

# msg = 'グローバル変数'

# def func():
#     msg = 'ローカル変数'
#     print(f'ローカルで{msg}')  #ローカルでローカル変数

# func()

# print(f'グローバルで{msg}') #グローバルでグローバル変数




## 組み込み関数list
# print(list(range(1, 10)))    

# def func():
#     # 組み込み関数を上書きしないように
#     # list = [1, 2, 3]
#     # print(list)
#     print(list(range(1, 10)))  #TypeErrorになる
    
# func()



# tax_rate = 0.1
# price = 100
# print(int(price * (1 + tax_rate)))

# str_date = '2023/01/10'
# print(str_date.split('/')[0])


# def get_tax_included(price):
#     tax_rate = 0.1
#     return int(price * (1 + tax_rate))

# def get_year(str_date):
#     return str_date.split('/')[0]

# print(get_tax_included(100))
# print(get_year('2023/01/10'))


# def get_area(x, y=4):
#     return x * y

# print(get_area(7, 3))
# print(get_area(5))


# # 演習1-07
# def tax_included_price(amount, tax_rate=10):
#     """
#     金額と税率を引数に受け取り、税込価格を返します。
#     税率は省略可能で、デフォルト値は 10% です。
#     :param amount: 税抜き金額
#     :param tax_rate: 税率（省略可能、デフォルト値は 10%）
#     :return: 税込価格
#     """
#     return amount * (1 + tax_rate / 100)

# def main():
#     """
#     ユーザーに税抜き金額と税率を入力してもらい、税込価格を出力します。
#     """
#     amount = float(input("税抜き金額を入力してください: "))
#     tax_rate_input = input("税率を入力してください（省略可、デフォルトは 10%）: ")

#     if tax_rate_input:
#         tax_rate = float(tax_rate_input)
#         total = tax_included_price(amount, tax_rate)
#     else:
#         total = tax_included_price(amount)

#     print(f"税込価格は {total:.2f} です。")

# if __name__ == "__main__":
#     main()

# def print_positional_args(*args):
#     print(args)

# print_positional_args(10, 30, 20, 40)
# print_positional_args('Bob', 'Tom')

# def print_keyword_args(**kwargs):
#     print(kwargs)

# print_keyword_args(name='Bob', gender='male', age=25)


# 演習1-10
# def product(*args):
#     """
#     任意の数の整数を引数に受け取り、その総乗を求めます。
#     :param args: 総乗を求める整数のリスト（可変長引数）
#     :return: 総乗の結果
#     """
#     result = 1
#     for num in args:
#         result *= num
#     return result

# def main():
#     """
#     ユーザーに任意の数の整数を入力してもらい、その総乗を出力します。
#     """
#     numbers = input("スペース区切りで整数を入力してください: ")
#     int_list = list(map(int, numbers.split()))
#     total_product = product(*int_list)
#     print(f"入力された整数の総乗は {total_product} です。")

# if __name__ == "__main__":
#     main()


# 演習1-11
# def key_value_tuples(**kwargs):
#     """
#     可変長キーワード引数を受け取り、キーと値のセットをタプルとするリストを生成して返します。
#     :param kwargs: キーワード引数（可変長）
#     :return: キーと値のセットをタプルとするリスト
#     """
#     return [(k, v) for k, v in kwargs.items()]

# def main():
#     """
#     ユーザーに任意の数のキーと値のペアを入力してもらい、
#     キーと値のセットをタプルとするリストを出力します。
#     """
#     user_input = input("キーと値のペアをコロン区切りで入力し、ペアはスペースで区切ってください（例: a:1 b:2）: ")
#     input_pairs = user_input.split()

#     kwargs = {}
#     for pair in input_pairs:
#         key, value = pair.split(':')
#         kwargs[key] = value

#     result = key_value_tuples(**kwargs)
#     print(f"生成されたタプルのリスト: {result}")

# if __name__ == "__main__":
#     main()


# def func():
#     return
#     print('出力されるかな？')

# print(func())


# def get_year(str_date: str, delimiter: str='/') -> int:
#     """日付を表す文字列から年を整数で返す
   
#     パラメータ:
#         str_date -- 日付を表す文字列
#         delimiter -- 区切り文字
#     戻り値:
#         年を表す整数
#     """
#     return int(str_date.split(delimiter)[0])

# print(get_year('2022-01-10', '-'))
# help(get_year) #関数などのドキュメントを表示する


# # 演習 1-14
# def is_leap_year(year: int) -> bool:
#     """
#     与えられた西暦年がうるう年であるかどうかを判定します。

#     :param year: 西暦年
#     :return: うるう年であれば True、そうでなければ False
#     """
#     if year % 4 != 0:
#         return False
#     if year % 100 != 0:
#         return True
#     if year % 400 != 0:
#         return False
#     return True


# def main():
#     """
#     ユーザーに西暦年を入力してもらい、その年がうるう年かどうかを判定し、結果を出力します。
#     """
#     year_input = int(input("西暦年を入力してください: "))
#     if is_leap_year(year_input):
#         print(f"{year_input}年はうるう年です。")
#     else:
#         print(f"{year_input}年はうるう年ではありません。")


# if __name__ == "__main__":
#     main()




# # 演習1-17
# def create_multiplication_table() -> list:
#     """
#     九九の計算結果を表す二次元リストを生成します。
#     :return: 二次元リスト
#     """
#     return [[i * j for j in range(1, 10)] for i in range(1, 10)]


# def main():
#     """
#     九九の計算結果を表す二次元リストを生成し、出力します。
#     """
#     multiplication_table = create_multiplication_table()
#     for row in multiplication_table:
#         print(row)


# if __name__ == "__main__":
#     main()

# # 演習1-19
# def count_characters(input_string: str) -> dict:
#     """
#     入力された文字列に含まれる文字をキー、その出現回数を値とする辞書を生成します。
#     :param input_string: 文字列
#     :return: 文字と出現回数の辞書
#     """
#     return {char: input_string.count(char) for char in set(input_string)}


# def main():
#     """
#     標準入力から入力された文字列に含まれる文字をキー、その出現回数を値とする辞書を生成し、出力します。
#     """
#     input_string = input("文字列を入力してください: ")
#     character_count = count_characters(input_string)
#     print(character_count)


# if __name__ == "__main__":
#     main()



# 演習1-21
def sort_scores(scores: list) -> list:
    """
    与えられた名前と点数の組を要素とした二次元リストを点数（降順）によって並び替えます。
    :param scores: 名前と点数の組を要素とした二次元リスト
    :return: 並び替えられた二次元リスト
    """
    return sorted(scores, key=lambda x: x[1], reverse=True)


def main():
    """
    名前と点数の組を要素とした二次元リストを点数（降順）によって並び替え、結果を出力します。
    """
    scores = [['Bob', 75], ['Tom', 88], ['Ivy', 83]]
    sorted_scores = sort_scores(scores)
    print(sorted_scores)


if __name__ == "__main__":
    main()