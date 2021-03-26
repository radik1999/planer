from datetime import date, timedelta
today = date.today() - timedelta(days=4)
print(today, date.weekday(today))
