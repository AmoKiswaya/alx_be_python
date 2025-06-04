FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
user_temp = input("Enter the temperature to convert: ")
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if user_temp.isdigit():
    user_temp = int(user_temp)
else:
    print("Invalid temperature. Please enter a numeric value")
    exit()

def convert_to_celsius(fahrenheit):
    global  FAHRENHEIT_TO_CELSIUS_FACTOR
    global user_temp
    result = (user_temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{user_temp} is {result}") 

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    global user_temp
    result = user_temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32 
    print(f"{user_temp} is {result}") 

if choice == "F":
    convert_to_celsius(fahrenheit=user_temp)
else:
    convert_to_fahrenheit(celsius=user_temp)

