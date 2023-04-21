from datetime import datetime

dt = datetime.now()
print(dt)

print('年', dt.year)
print('月', dt.month)
print('日', dt.day)
print('時', dt.hour)
print('分', dt.minute)
print('秒', dt.second)
print('曜日', dt.weekday())

print(datetime(2023, 4, 21, 21, 15, 0))
