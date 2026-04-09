
def calculate_total(base_price, toppings, delivery_fee):
    """Calculate the total cost of the pizza order."""
    subtotal = base_price + toppings
    tax = subtotal * 0.08
    total = subtotal + tax + delivery_fee
    return total

def format_receipt(name, total):
    """Format the receipt for the pizza order."""
    receipt = f"Order for {name} Total: ${total:.2f}"
    return receipt

def main():
    name = input("Enter your name: ")
    base_price = float(input("Base pizza price: "))
    num_toppings = int(input("How many toppings? "))
    delivery = input("Delivery? (y/n): ")


    toppings = num_toppings * 1.5
    delivery_fee = 3 if delivery == 'y' else 0

    total = calculate_total(base_price, toppings, delivery_fee)
    receipt = format_receipt(name, total)
    print(receipt)

if __name__ == "__main__":
    main()