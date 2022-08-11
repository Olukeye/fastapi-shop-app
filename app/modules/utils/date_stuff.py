from datetime import  datetime, date, timedelta

def create_customised_datetime():
    today = datetime.now()
    date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time