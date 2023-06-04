import datetime

def parse_date(date):
    adjusted_datetime = date - datetime.timedelta(hours=3)
    formatted_datetime = adjusted_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime