from datetime import date, timedelta
today = date.today()
print(today - timedelta(days=today.weekday()))
