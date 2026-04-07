# Player Interface

This module provides a simple `Player` base class and a concrete `Pawn` implementation for grid-based movement.

## Overview

- `Player` (abstract): holds movement vectors in `moves`, current `position`, movement `history`, and `path` of positions visited. `make_move()` applies a movement vector to update position. `level_up()` is abstract.
- `Pawn` (concrete): starts with orthogonal moves (up, down, left, right) and its `level_up()` adds diagonal moves.

## Usage

Place `player.py` in your project and import the classes:

```python
from player import Pawn

p = Pawn()
print('start:', p.position)

# Make a few moves using available move vectors
for _ in range(3):
    p.make_move()

print('position after 3 moves:', p.position)
print('path:', p.path)
print('history (dx,dy):', p.history)

# Level up to add diagonal moves, then move again
p.level_up()
p.make_move()
print('position after level up and one move:', p.position)
```

## API

- `moves` (list[tuple[int,int]]): movement vectors available to the player, e.g. `(0, 1)` for up.
- `position` (tuple[int,int]): current (x, y) position.
- `path` (list[tuple[int,int]]): list of positions visited, starting with the initial position.
- `history` (list[tuple[int,int]]): list of applied movement vectors in order.
- `make_move()` -> tuple[int,int]: choose a movement vector from `moves` (or a fallback set) and apply it.
- `level_up()` -> None: abstract in `Player`; in `Pawn` it extends `moves` with diagonal vectors.

## Notes

- `make_move()` uses tuples for movement; if `moves` is empty it falls back to orthogonal moves.
- Adjust `moves` directly on instances if you want custom movement sets.
