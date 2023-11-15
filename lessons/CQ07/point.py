
"""CQ07 - Intro to Object Oriented Programming."""
from __future__ import annotations
__author__ = "730561330"


class Point:
    """Represents a point on the 2-D Cartesian plane."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Point's constructor."""
        self.x = x_init
        self.y = y_init
    
    def __str__(self) -> str:
        """Returns a string of the point's coordinates."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Returns a new point with factor scaled attributes."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Returns a new point with attributes added to a factor."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    
    # CQ07
    def scale_by(self, factor: int):
        """Mutates point by scaling x and y attributes by 'factor'."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new point with factor-scaled attributes."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point