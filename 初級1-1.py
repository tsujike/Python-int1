print("Hello Python!!")

print(123)

num = 123
print(num)

print(type(123.4))
print(type([]))
print(type(()))
print(type({}))

x = 1
x += 1
print(x)

msg = "Hello"
print(msg[1:5:1])

# 1-10
name = "Kenny"
msg = f'{name}様\nお世話になっております。\nよろしくお願いいたします。\n\n高橋'
print(msg)

# 1-14
h = 10
w = 100
area = h * w
msg = f'縦は{h}cm,横は{w}cm,面積は{area}平方cmです。'
print(msg)

# 1-15
x = 10
y = 3
mod = x % y
msg = f'{x}を{y}で割ったときの余りは{mod}です。'
print(msg)




# 2-03
x = 9
if x%2 == 0:
    print(f'{x}は偶数です')
else:
    print(f'{x}は奇数です')

# 2-06
rank = 50
if rank > 90:
    print("すごい")
elif rank < 89 and 75 <= rank:
    print("がんばりましたね")
elif rank < 74 and 50 <= rank:
    print("ギリギリでしたね")
elif rank < 50:
    print("残念でした")

print("test")

# 2-09
def main():
    """
    x の値を 1 から開始し、2, 4, 8, ... と倍々にしていきながら、
    x の値を出力するプログラムです。
    x の値が 100 を超えた最初の数まで実行します。
    """
    x = 1
    while x <= 100:
        print(x)
        x *= 2

    print(x)


if __name__ == "__main__":
    main()

# 2-12
def sum_numbers(end):
    """
    1 から end までの整数を順番に加算し、その結果を返します。
    :param end: 加算を終了する整数
    :return: 1 から end までの整数の和
    """
    total = sum(range(1, end + 1))
    return total

def main():
    """
    ユーザーに入力を求め、1 からその入力値までの整数を加算し、
    結果を「1 から ● まで加算すると XX です。」の形式で出力します。
    """
    # end = int(input("1 から何までの整数を加算しますか？: "))
    # total = sum_numbers(end)
    # print(f"1 から {end} まで加算すると {total} です。")

if __name__ == "__main__":
    main()

#2-14
def main():
    """
    九九の表を出力します。各行は、
    「a × b = 結果」という形式で表示されます。
    """
    for a in range(1, 10):
        for b in range(1, 10):
            result = a * b
            print(f"{a} × {b} = {result}")

if __name__ == "__main__":
    main()

#2-15
def fizz_buzz(n):
    """
    1 から n までの数値を FizzBuzz ルールに従って出力します。
    :param n: FizzBuzz 処理を行う最大の整数
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    """
    ユーザーに入力を求め、1 からその入力値まで FizzBuzz 処理を行い、結果を出力します。
    """
    n = int(input("FizzBuzz を実行する最大の整数を入力してください: "))
    fizz_buzz(n)

if __name__ == "__main__":
    main()

#2-18
def triangle_area(x,y):
    """
    底辺 x と高さ y の三角形の面積を計算し、その結果を返します。
    :param x: 三角形の底辺の長さ
    :param y: 三角形の高さ
    :return: 三角形の面積
    """
    return 0.5 * x * y
    
#2-19
def is_even():
    """
    与えられた整数が偶数であるかどうかを判定します。
    :param x: 判定対象の整数
    :return: 偶数の場合は True、そうでない場合は False
    """
    return x % 2 == 0



#3-4
def check_membership(members1, members2):
    """
    members2 の各要素について、それが members1 に含まれていれば
    「○○はメンバーです」と出力し、そうでなければ
    「○○はメンバーではありません」と出力します。
    :param members1: メンバーリスト1
    :param members2: メンバーリスト2
    """
    for member in members2:
        if member in members1:
            print(f"{member}はメンバーです")
        else:
            print(f"{member}はメンバーではありません")

def main():
    members1 = ['Bob', 'Tom', 'Ivy', 'Jay']
    members2 = ['Bob', 'Tim']
    check_membership(members1, members2)

if __name__ == "__main__":
    main()

#3-7
def generate_list():
    """
    1 から 9 までの整数で構成されるリストを生成します。
    :return: 生成されたリスト
    """
    return list(range(1, 10))

def generate_multiplication_table():
    """
    九九の各段の積によるリストを要素とする二次元リストを生成します。
    :return: 生成された二次元リスト
    """
    table = []
    for i in range(1, 10):
        row = [i * j for j in range(1, 10)]
        table.append(row)
    return table

def main():
    simple_list = generate_list()
    multiplication_table = generate_multiplication_table()

    print("1 から 9 までの整数で構成されるリスト:")
    print(simple_list)

    print("九九の各段の積によるリストを要素とする二次元リスト:")
    for row in multiplication_table:
        print(row)

if __name__ == "__main__":
    main()


#3-14
def add_key_value_pair(person, key, value):
    """
    辞書 person に任意のキーと値のペアを要素として追加します。
    キーが存在していなければ、辞書にペアを追加し、「キー〇〇と値××を追加しました。」と表示します。
    既にキーが存在していれば、「既にキー〇〇が存在しています。」と表示します。
    :param person: 対象となる辞書
    :param key: 追加するキー
    :param value: 追加する値
    """
    if key in person:
        print(f"既にキー{key}が存在しています。")
    else:
        person[key] = value
        print(f"キー{key}と値{value}を追加しました。")

def main():
    person = {'name': 'Bob', 'gender': 'male', 'age': 25}
    add_key_value_pair(person, 'city', 'New York')
    add_key_value_pair(person, 'age', 30)

    print(person)

if __name__ == "__main__":
    main()



#3-15
def count_onigiris(onigiris):
    """
    おにぎりの種類名をキー、登場回数を値とする辞書を生成します。
    :param onigiris: おにぎりの種類名が格納されたリスト
    :return: おにぎりの種類名と登場回数の辞書
    """
    onigiri_count = {}
    for onigiri in onigiris:
        if onigiri in onigiri_count:
            onigiri_count[onigiri] += 1
        else:
            onigiri_count[onigiri] = 1
    return onigiri_count

def main():
    onigiris = [
        'シャケ', 'ツナ', 'ツナ', 'コンブ', 'シャケ', 'オカカ',
        'シャケ', 'ツナ', 'コンブ', 'シャケ'
    ]
    onigiri_count = count_onigiris(onigiris)
    print(onigiri_count)

if __name__ == "__main__":
    main()

#4-3
def create_member_favorite_dict(members, favorites):
    """
    メンバーの名前をキー、お気に入りのフルーツを値とする辞書を生成します。
    :param members: メンバーの名前が格納されたリスト
    :param favorites: お気に入りのフルーツが格納されたリスト
    :return: メンバーの名前とお気に入りのフルーツの辞書
    """
    if len(members) != len(favorites):
        raise ValueError("メンバーの数とお気に入りの数が一致しません")

    member_favorite_dict = {}
    for member, favorite in zip(members, favorites):
        member_favorite_dict[member] = favorite

    return member_favorite_dict

def main():
    members = ['Bob', 'Tom', 'Ivy']
    favorites = ['apple', 'orange', 'grape']

    member_favorite_dict = create_member_favorite_dict(members, favorites)
    print(member_favorite_dict)

if __name__ == "__main__":
    main()


#4-9
def count_onigiris_from_string(data):
    """
    文字列データから、おにぎりの名前をキー、登場した回数を値とする辞書を生成します。
    :param data: おにぎりの名前がカンマ区切りで格納された文字列
    :return: おにぎりの名前と登場回数の辞書
    """
    onigiri_count = {}
    onigiris = data.split(',')

    for onigiri in onigiris:
        if onigiri in onigiri_count:
            onigiri_count[onigiri] += 1
        else:
            onigiri_count[onigiri] = 1

    return onigiri_count

def main():
    data = 'シャケ,ツナ,ツナ,コンブ,シャケ,オカカ,シャケ,ツナ,コンブ,シャケ'
    onigiri_count = count_onigiris_from_string(data)
    print(onigiri_count)

if __name__ == "__main__":
    main()


#4-10
def count_rps_inputs():
    """
    ユーザーから「rock」「scissors」「paper」の入力を受け付け、
    入力のたびにそれぞれ何回入力があったかを表示します。
    「end」が入力されたらプログラムを終了します。
    """
    valid_inputs = {'rock', 'scissors', 'paper'}
    input_count = {'rock': 0, 'scissors': 0, 'paper': 0}

    while True:
        user_input = input("rock, scissors, paper, or end: ").lower()

        if user_input == 'end':
            break
        elif user_input in valid_inputs:
            input_count[user_input] += 1
            print(f"Input count: {input_count}")
        else:
            print("Invalid input. Please try again.")

def main():
    count_rps_inputs()

if __name__ == "__main__":
    main()


