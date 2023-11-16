"""File to define River class."""

__author__ = "730561330"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """A river in the wild that contains fish and bears."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of bears and fish and gets rid of those that are too old."""
        # Removes fish that are older than 3
        fish_alive: list[Fish] = []
        for x in range(0, len(self.fish)):
            if self.fish[x].age <= 3:
                fish_alive.append(self.fish[x])
        self.fish = fish_alive
        # Removes bears that are older than 5
        bears_alive: list[Bear] = []
        for x in range(0, len(self.bears)):
            if self.bears[x].age <= 5:
                bears_alive.append(self.bears[x])
        self.bears = bears_alive
        return None

    def remove_fish(self, amount: int):
        """Removes a specific number of fish from the river."""
        fish_alive: list[Fish] = []
        i: int = 0
        while i < len(self.fish):
            fish_alive.append(self.fish[i]) 
            i += 1
        self.fish = fish_alive
        return None

    def bears_eating(self):
        """Simulates a bear eating the fish on the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bears from the river when they are starved."""
        bears_alive: list[Bear] = []
        i: int = 0
        while i < len(self.bears):
            if self.bears[i].hunger_score >= 0:
                bears_alive.append(self.bears[i])
            i += 1
        self.bears = bears_alive
        return None
        
    def repopulate_fish(self):
        """For every pair of fish they reproduce 4 more."""
        og_fish_pop: int = len(self.fish)
        i: int = 0
        while 1 < (og_fish_pop // 2) * 4:
            self.fish.append(Fish())
            i += 1
        return None
    
    def repopulate_bears(self):
        """For every pair of bears they reproduce 1 more."""
        og_bear_pop: int = len(self.bears)
        i: int = 0
        while i < og_bear_pop // 2:
            self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self):
        """Updates user on the river's fish and bear count, as well as the day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
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
        """Runs seven days on the river to simulate a week."""
        i: int = 0
        while 1 <= 7:
            self.one_river_day()
            i += 1
        return None