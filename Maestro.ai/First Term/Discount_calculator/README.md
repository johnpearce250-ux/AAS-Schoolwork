# Discount Calculator

A small Python example that demonstrates a strategy-based discount engine for products. The project calculates the best (lowest) price for a product given multiple discount strategies and a user tier.

## Features

- Strategy-based discount system using `DiscountStrategy` subclasses.
- Example strategies included: percentage discounts, fixed-amount discounts, and a premium-user discount.
- Simple engine `DiscountEngine` that evaluates applicable strategies and returns the best price.

## Requirements

- Python 3.8 or newer
- No external dependencies

## Files

- [Discount_Calculator.py](Discount_Calculator.py#L1-L200) — main implementation and example run

## Quick start

Run the example from the repository root:

```bash
python Discount_Calculator.py
```

You should see output similar to:

```
Best price for Wireless Mouse for Premium user: $40.00
```

## How it works (brief)

- `Product` represents an item with a `name` and `price`.
- `DiscountStrategy` is an abstract base class. Each strategy implements `is_applicable(product, user_tier)` and `apply_discount(product)`.
- Included strategies:
  - `PercentageDiscount(percent)` — applies a percent-off price.
  - `FixedAmountDiscount(amount)` — subtracts a fixed amount from the product price.
  - `PremiumUserDiscount()` — applies a 20% discount for premium users.
- `DiscountEngine` accepts a list of strategies and returns the lowest price from either the original price or any applicable discounted prices.

## Example: using the engine programmatically

```python
from Discount_Calculator import Product, DiscountEngine, PercentageDiscount, FixedAmountDiscount, PremiumUserDiscount

product = Product("Keyboard", 80.0)
strategies = [PercentageDiscount(15), FixedAmountDiscount(10), PremiumUserDiscount()]
engine = DiscountEngine(strategies)
best = engine.calculate_best_price(product, "regular")
print(f"Best price: ${best:.2f}")
```

## Extending

To add a new discount rule, create a class that inherits `DiscountStrategy`, implement `is_applicable` and `apply_discount`, then add an instance to the strategies list passed to `DiscountEngine`.

## License

MIT
