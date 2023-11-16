"""File to define Bear class"""


class Bear:
    """A bear with a specific age, and a hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Bears Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """With every day the bear gets older and hungrier"""
        self.age += 1 
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear getting them goods!"""
        self.hunger_score += num_fish
        return None
