num1 = int(input("Enter the first number: "))
operator = input("Choose the opertion (+, -, *, /): ")
num2 = int(input("Enter the second number: "))


match operator:
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

        