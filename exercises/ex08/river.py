"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:

    day: int
    bears: list[str]
    fish: list[str]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        for x in range(0, len(self.fish)):
            if self.fish.age > 3:
                self.fish.pop()
        for x in range(0, len(self.bears)):
            if self.bears.age > 5:
                self.bears.pop()
        return None

    def remove_fish(self, amount: int):
        for fish in range(0, amount):
            self.fish.pop(0) 
        return None

    def bears_eating(self):
        if len(self.fish) >5 :
            for bears in self.bears:
                self.remove_fish(3)
                self.eat(3)
        return None
    
    def check_hunger(self):
        for bear in self.bears:
            if Bear.hunger_score < 0:
                self.bears.pop()
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        print(f"~~~ Day{self.day} ~~~")
        print(f"Fish Population: {self.fish}")
        print(f"Bear Population: {self.bears}")
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a day of life in the river"""
        for river_day in range(0,7):
            self.one_river_day()
        return None
            
