from dataclasses import dataclass
from math import hypot

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    name: str|None = None

    # implementation de la builtin fonction str
    def __str__(self) -> str:
        return f"{self.name}({self.x}, {self.y})"

    def distance(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)