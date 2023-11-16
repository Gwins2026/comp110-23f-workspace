"""File to define Fish class."""

class Fish:
    """A fish with a specific age."""
    
    age: int

    def __init__(self):
        """Fish's Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish grows older."""
        self.age += 1
        return None