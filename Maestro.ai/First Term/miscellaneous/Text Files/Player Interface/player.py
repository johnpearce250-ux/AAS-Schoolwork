from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.history = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        # Choose a movement vector from available moves (tuples).
        # If no moves are defined (base Player), fallback to orthogonal moves.
        possible = self.moves if self.moves else [(0, 1), (0, -1), (-1, 0), (1, 0)]
        dx, dy = random.choice(possible)

        x, y = self.position
        x += dx
        y += dy

        self.position = (x, y)
        self.path.append(self.position)
        self.history.append((dx, dy))
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Orthogonal moves: up, down, left, right (1 unit each)
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def level_up(self):
        # Add diagonal moves: down-left, down-right, up-left, up-right
        diagonals = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        self.moves.extend(diagonals)
        
        


