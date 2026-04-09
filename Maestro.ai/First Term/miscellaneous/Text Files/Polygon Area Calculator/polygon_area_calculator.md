**Polygon Area Calculator — Documentation**

Brief reference for the `Rectangle` and `Square` classes in `polygon_area_calculator.py`.

**Overview**:
- **Rectangle**: Represents a rectangle with `width` and `height` and methods for area, perimeter, diagonal, an ASCII picture, and fitting another shape inside.
- **Square**: Subclass of `Rectangle` where both sides are equal. Provides `set_side` convenience method.

**Rectangle**
- **Constructor**: `Rectangle(width, height)` — create a rectangle.
- **Methods**:
  - `set_width(width)`: set `width`.
  - `set_height(height)`: set `height`.
  - `get_area()`: returns area (width * height).
  - `get_perimeter()`: returns perimeter (2*(width + height)).
  - `get_diagonal()`: returns diagonal length using Pythagoras.
  - `get_picture()`: returns an ASCII-art rectangle using `*`; returns "Too big for picture." if width or height > 50.
  - `get_amount_inside(shape)`: returns how many times `shape` fits inside this rectangle (uses integer division on dimensions).
  - `__str__()`: returns `Rectangle(width=..., height=...)`.

**Square (subclass of Rectangle)**
- **Constructor**: `Square(side)` — creates a square by calling `Rectangle(side, side)`.
- **Methods**:
  - `set_side(side)`: set both width and height to `side`.
  - `set_width(width)` / `set_height(height)`: overridden to keep square invariant (they call `set_side`).
  - `__str__()`: returns `Square(side=...)`.

**Usage examples**
```python
from polygon_area_calculator import Rectangle, Square

# Rectangle
r = Rectangle(4, 3)
print(r.get_area())        # 12
print(r.get_perimeter())   # 14
print(r.get_diagonal())    # 5.0
print(r.get_picture())
# ****
# ****
# ****

# Square
s = Square(5)
print(s.get_area())        # 25
print(s)                   # Square(side=5)

# How many small rectangles fit in a larger one
big = Rectangle(10, 8)
small = Rectangle(3, 2)
print(big.get_amount_inside(small))  # (10//3) * (8//2) = 3 * 4 = 12

# Picture size guard
huge = Rectangle(60, 2)
print(huge.get_picture())  # "Too big for picture."
```

**Notes**
- `get_amount_inside` uses floor division of dimensions; it does not rotate shapes.
- `get_picture` limits the drawn size to prevent huge output.

