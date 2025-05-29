num1 = int(input("Enter the first number: "))
operation = input("Choose the operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))


match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.") 
    case "-":
        if num1 < num2:
            result = num2 - num1
            print(f"The result is {result}.") 
        else:
            result = num1 - num2
            print(f"The result is {result}.") 
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.") 
        elif num1 > num2:
            result = num1 / num2
            print(f"The result is {result}.") 
        else:
            result = num2 / num1
            print(f"The result is {result}.") 

        