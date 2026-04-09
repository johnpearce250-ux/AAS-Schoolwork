raw_lines = ["$100.12", " 200", "30.05", "N/A", "500.41 "]

def sanitize(lines):
    """Convert raw input lines to a list of valid float amounts."""
    amounts = []
    for line in lines:
        line = line.strip().replace("$", "").replace("N/A", "")
        if line:  # Only add non-empty strings
            amounts.append(line)
    return amounts

def to_numbers(lines):
    """Convert sanitized lines to floats."""
    numbers = []
    for line in lines:
        number = float(line)
        numbers.append(number)
    return numbers

def total_sales(amounts):
    """Calculate the total sales from a list of amounts."""
    total = 0
    for amount in amounts:
        """Ensure that each amount is a valid number and add it to the total."""
        if not isinstance(amount, (int, float)):
            raise ValueError(f"All amounts must be numbers.")
        total += amount  
    return total

def format_usd(amount):
    """Format a number as USD currency."""
    return f"${amount:.2f}"

def main():
    """Main function to process sales data."""
    sanitized = sanitize(raw_lines)
    numbers = to_numbers(sanitized)
    total = total_sales(numbers)
    print(f"Sales total: {format_usd(total)}")
    
if __name__ == "__main__":
    main()