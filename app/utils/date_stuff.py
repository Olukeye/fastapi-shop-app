from datetime import  datetime, date, timedelta

def create_customised_datetime():
    today = datetime.now()
    date_time = today.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time