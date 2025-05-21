import datetime

current_year = datetime.datetime.now().year
current_age = int(input("How old are you? "))
future_year = 2050

years_left = future_year - current_year
future_age = current_age + years_left

print(f"In {future_year}, you will be {future_age} years old.")


