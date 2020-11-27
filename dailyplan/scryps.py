from datetime import date, timedelta


def date_convert(value):
    value_date = map(int, value.split('-'))
    value_date = date(*value_date)
    return value_date


def time_convert(value):
    minutes = value % 60
    hours = value // 60
    return '{}:{:0>2}'.format(hours, minutes)


if __name__ == '__main__':
    print(time_convert(130))

