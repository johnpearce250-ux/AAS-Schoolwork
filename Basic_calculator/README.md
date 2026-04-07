# Basic Calculator Program

## Overview
A simple command-line calculator that performs basic arithmetic operations. The program runs in a loop, accepting user input until the user chooses to quit.

## Features
- ✅ **Four Operations**: Addition, subtraction, multiplication, and division
- ✅ **Input Validation**: Prevents crashes from invalid number input
- ✅ **Case-Insensitive**: Operations work regardless of capitalization (e.g., "Add", "ADD", "add")
- ✅ **Error Handling**: Detects division by zero and invalid operations
- ✅ **Clean UX**: Whitespace trimming and helpful error messages
- ✅ **Immediate Exit**: Type "quit" to exit without entering numbers

## How to Use

1. Run the program:
   ```bash
   python basic_calculator.py
   ```

2. Follow the prompts:
   - Enter an operation: `add`, `subtract`, `multiply`, or `divide`
   - Enter two numbers when prompted
   - View the result

3. Exit the program:
   - Type `quit` to exit at any time

### Example Session
```
Enter the operation (add, subtract, multiply, divide), or 'quit' to exit: add
Enter the first number: 5
Enter the second number: 3
The result is: 8

Enter the operation (add, subtract, multiply, divide), or 'quit' to exit: quit
Goodbye!
```

## Function Descriptions

### `get_user_input()`
Prompts the user for an operation and two numbers.

**Returns:**
- `(operation, number_1, number_2)` - Tuple of operation (str) and two floats
- `(None, None, None)` - If user enters "quit"

**Features:**
- Converts operation to lowercase and strips whitespace
- Validates numeric input with try/except block
- Retries if invalid numbers are entered

### `calculate_total(operation, number_1, number_2)`
Performs the requested arithmetic operation.

**Parameters:**
- `operation` (str): One of "add", "subtract", "multiply", or "divide"
- `number_1` (float): First operand
- `number_2` (float): Second operand

**Returns:**
- `float` - Result of the calculation
- `str` - Error message if operation is invalid or division by zero occurs

**Supported Operations:**
| Operation | Symbol | Example |
|-----------|--------|---------|
| add | + | 5 + 3 = 8 |
| subtract | - | 5 - 3 = 2 |
| multiply | × | 5 × 3 = 15 |
| divide | ÷ | 6 ÷ 3 = 2 |

### `print_result(result)`
Displays the calculation result to the user.

**Parameters:**
- `result` - The value to display (can be float or error message string)

### `main()`
Controls the program flow with a loop that continues until the user quits.

**Flow:**
1. Get user input
2. Check if quit command
3. Calculate result
4. Print result
5. Loop back to step 1

## Error Handling

| Error | Message | Cause |
|-------|---------|-------|
| Invalid Numbers | "Error: Please enter valid numbers." | Non-numeric input entered |
| Division by Zero | "Error: Division by zero" | Attempted to divide by 0 |
| Invalid Operation | "Error: '{operation}' is not a valid operation..." | Unsupported operation entered |

## Code Structure

```
basic_calculator.py
├── get_user_input()      # Handles user input
├── calculate_total()     # Performs calculations
├── print_result()        # Displays output
└── main()                # Program flow control
```

## Requirements
- Python 3.x or later
- No external dependencies

## License
Open source - feel free to modify and distribute
