print("Welcome To Simple Calculator \n----------------------------------")
print("Enter 'exit' to quit \n----------------------------------")

while True:
    user_input = input("Enter expression: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye! \n----------------------------------")
        break
    
    expression = user_input.replace('×', '*').replace('÷', '/')
    
    try:
        result = eval(expression)
        formatted_expression = expression.replace('*', '×').replace('/', '÷')
        print(f"Expression Entered: {formatted_expression} \n---------------------------------- \nResult: {result} \n----------------------------------")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except:
        print("Error: Invalid expression")