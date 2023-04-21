from datetime import datetime

dt = datetime.now()
print(dt.strftime('%Y年%m月%d日 %H時%M分%S秒'))
print(dt.strftime('%Y/%m/%d(%a) %H:%M:%S'))
print(dt.strftime('%x %X'))

