from datetime import datetime, timedelta

dt = datetime.now()
print(dt)

td1 = timedelta(weeks=1)
print(dt + td1)

td2 = timedelta(days=3, hours=2)
print(dt - td2)