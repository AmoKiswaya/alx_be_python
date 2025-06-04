from datetime import datetime, timedelta

def display_current_datetime ():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

display_current_datetime()

def calculate_future_date ():
    current_date = datetime.now().date()
    user_days = int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + timedelta(days=user_days)
    format_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {format_future_date}") 

calculate_future_date()


