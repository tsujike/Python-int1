# 演習３－18
# 
# 以下の関数を作成してみましょう。
# datetimeオブジェクトを受け取り、その月の月初の日付をdatetimeオブジェクトで返す関数
# datetimeオブジェクトを受け取り、その月の月末の日付をdatetimeオブジェクトで返す関数

from datetime import datetime, timedelta

def month_start(dt):
    return dt.replace(day=1)

def month_end(dt):
    next_month_start = dt.replace(day=28) + timedelta(days=4)  # 最も遠い月末日に移動
    return next_month_start - timedelta(days=next_month_start.day)  # 次の月の初めに戻って、1日引く

# テスト
dt = datetime(2023, 1, 15)

start_of_month = month_start(dt)
print(start_of_month)  # 2023-01-01 00:00:00

end_of_month = month_end(dt)
print(end_of_month)  # 2023-01-31 00:00:00