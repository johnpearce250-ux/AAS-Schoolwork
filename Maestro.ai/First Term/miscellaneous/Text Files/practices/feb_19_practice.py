def compute_subtotal(prices):
    return sum(prices)

def add_tax(subtotal):
    taxed_total = subtotal * 1.08
    return taxed_total

def main():
    prices = [12, 8, 5]
    subtotal=compute_subtotal(prices)
    total = add_tax(subtotal)
    print("Total with tax:", total)

main()