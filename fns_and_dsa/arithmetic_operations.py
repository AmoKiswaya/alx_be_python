def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            if num1 > num2:
                return num1 - num2
            else:
                return num2 - num1 
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 > num2:
                return num1 / num2
            else:
                return num2 / num1 
        case _:
            return "Invalid choice" 
    

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation) 
print(f"Result: {result}")

        
    