# 演習３－19
# 
# 以下の機能を持つクラスDateobjectを作成してください。
# 
# コンストラクタ: datetimeオブジェクトを渡すとインスタンスを生成する
# インスタンス変数value: datetimeオブジェクト
# 「2023年01月01日 (日)」という形式の文字列を返すメソッド
# 月初の日付を「2023/01/01」という形式の文字列として返すメソッド
# 月初の日付をdatetimeオブジェクトで返すメソッド
# 月末の日付をdatetimeオブジェクトで返すメソッド

from datetime import datetime, timedelta

class DateObject:
    def __init__(self, dt):
        self.value = dt

    def formatted_string(self):
        return self.value.strftime("%Y年%m月%d日 (%a)")

    def month_start_string(self):
        month_start_dt = self.value.replace(day=1)
        return month_start_dt.strftime("%Y/%m/%d")

    def month_start(self):
        return self.value.replace(day=1)

    def month_end(self):
        next_month_start = self.value.replace(day=28) + timedelta(days=4)
        return (next_month_start - timedelta(days=next_month_start.day)).replace(hour=0, minute=0, second=0, microsecond=0)

# テスト
dt = datetime(2023, 1, 15)
date_obj = DateObject(dt)

print(date_obj.formatted_string())  # 2023年01月15日 (Sun)
print(date_obj.month_start_string())  # 2023/01/01
print(date_obj.month_start())  # 2023-01-01 00:00:00
print(date_obj.month_end())  # 2023-01-31 00:00:00