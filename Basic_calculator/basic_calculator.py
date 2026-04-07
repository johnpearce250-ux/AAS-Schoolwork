previous_calcs = []
def get_user_input():
    """ Get the operation and numbers from the user.  Returns a tuple containing the operation and the two numbers. """
    operation = input("Enter the operation (add, subtract, multiply, divide), or 'quit' to exit, or 'history' to view previous calculations: ").strip().lower()
    
    if operation == "quit":
        return None, None, None
    elif operation == "history":
        print_previous_calculations()
        return get_user_input()
    elif operation not in ["add", "subtract", "multiply", "divide"]:
        print(f"Error: '{operation}' is not a valid operation. Please enter add, subtract, multiply, divide, or quit.")
        return get_user_input()
    
    while True:
        try:
            number_1 = float(input("Enter the first number: "))
            number_2 = float(input("Enter the second number: "))
            return operation, number_1, number_2
        except ValueError:
            print("Error: Please enter valid numbers.")

def calculate_total(operation, number_1, number_2):
    """Calculate the total based on the operation and numbers provided.  Returns the result of the calculation. """
    if operation == "add":
        return number_1 + number_2
    elif operation == "subtract":
        return number_1 - number_2
    elif operation == "multiply":
        return number_1 * number_2
    elif operation == "divide":
        if number_2 != 0:
            return number_1 / number_2
        else:
            return "Error: Division by zero"
    else:
        return f"Error: '{operation}' is not a valid operation. Use add, subtract, multiply, or divide."
    
def store_calculation(operation, number_1, number_2, result):
    """Store the calculation in the previous_calcs list.  Takes the operation, numbers, and result as arguments and appends a formatted string to the previous_calcs list. """
    calc_string = f"{number_1} {operation} {number_2} = {result}"
    previous_calcs.append(calc_string)

def print_previous_calculations():
    """Print the previous calculations.  Iterates through the previous_calcs list and prints each calculation to the console. """
    if previous_calcs:
        print("Previous calculations:")
        for calc in previous_calcs:
            print(calc)
    else:
        print("No previous calculations.")

def print_result(result):
    """Print the result of the calculation.  Takes the result as an argument and prints it to the console. """
    print(f"The result is: {result}")

def main():
    while True:
        operation, number_1, number_2 = get_user_input()
        
        if operation is None:
            print("Goodbye!")
            break
        
        result = calculate_total(operation, number_1, number_2)
        store_calculation(operation, number_1, number_2, result)
        print_result(result)
        print()

if __name__ == "__main__":
    main()   
    