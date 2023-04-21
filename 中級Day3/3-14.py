# 演習３－14

# 以下の関数を作成してみましょう。
# datetimeオブジェクトを受け取り「2023年01月01日 (日)」という形式の文字列を返す関数
# datetimeオブジェクトを受け取り、その月の月初の日付を「2023/01/01」という形式の文字列として返す関数

from datetime import datetime

def format_datetime_jp(dt):
    days = ["月", "火", "水", "木", "金", "土", "日"]
    return dt.strftime(f'%Y年%m月%d日 ({days[dt.weekday()]})')

def format_month_start(dt):
    return dt.replace(day=1).strftime('%Y/%m/%d')

# テスト
dt = datetime(2023, 1, 15)

formatted_dt_jp = format_datetime_jp(dt)
print(formatted_dt_jp)  # 2023年01月15日 (日)

formatted_month_start = format_month_start(dt)
print(formatted_month_start)  # 2023/01/01