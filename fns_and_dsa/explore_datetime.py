from datetime import datetime

def display_current_datetime():
    current_date_time = datetime.now()
    format_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {format_date_time}")

display_current_datetime()

def ask():
    days_to_add = input("Enter the number of days to add to the current date: ")
    return days_to_add

def integer(numbergiven):

    if numbergiven.isdigit():
        plus = int(numbergiven)
        return plus
    else:
        print("INVALID INPUT")


def calculate_future_date():
    
    current_date = datetime.today()
    future_date = current_date + datetime.timedelta(days = integer(ask()))
    print(f"Future date: {future_date}")

calculate_future_date()