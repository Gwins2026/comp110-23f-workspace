"""File to define Fish class"""

class Fish:
    
    age: int

    def __init__(self, age: int):
        self.age: int = 0
    
    def one_day(self):
        self.age += 1
        return None