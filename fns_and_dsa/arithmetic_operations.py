def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return abs(num1 - num2) 
        case "multiply":
            return num1 * num2
        case "divide":
            try:
                return abs(num1 / num2) 
            except ZeroDivisionError:
                return "Can't divide by zero"
        case _:
            return "Invalid choice" 
    

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation) 
print(f"Result: {result}") 


        
    