
def total_sales(amounts):
    """Calculate the total sales from a list of amounts."""
    total = 0
    for amount in amounts:
        """Ensure that each amount is a valid number and add it to the total."""
        if not isinstance(amount, (int, float)):
            raise ValueError(f"All amounts must be numbers.")
        total += amount  
    return total
def main():
    sales = []
    """User input for sales amounts, separated by commas."""
    amount = input("Enter amounts separted by commas: ") 
    for amount in amount.split(","):
        sales.append(float(amount.strip()))
    tax_rate = 0.07
    total = total_sales(sales)
    print(f"Sales total: ${total:.2f}")
    tax = total * tax_rate
    print(f"Tax: ${tax:.2f}")
    grand_total = total + tax
    print(f"Grand total: ${grand_total:.2f}")
    if grand_total > 500:
        print("Top earner!")

if __name__ == "__main__":
    main()