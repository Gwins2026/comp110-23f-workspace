"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730561330"


class Simpy:
    values: list[float]

    def __init__(self, val_initialize: list[float]):
        """Constructor for Simpy."""
        self.values = val_initialize

    def __str__(self) -> str:
        """Simpy's string magic method."""
        return f"Simpy({self.values})"

    def fill(self, val: float, num_vals: int):
        """Fills Simpy's values with a specfic number of repeating values."""
        self.values = []
        i: int = 0
        while i < num_vals:
            self.values.append(val)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values attribute with a range of values in terms of floats."""
        assert step != 0.0
        val: float = start
        while val != stop:
            self.values.append(val)
            val += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        sums: float = sum(self.values) 
        return sums

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic method/operator overload for addition."""
        output: Simpy = Simpy([])
        if type(rhs) == float:
            for x in range(0, len(self.values)):
                val: float = self.values[x] + rhs
                output.values.append(val)
        else:   # rhs is a Simpy
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                val: float = self.values[x] + rhs.values[x]
                output.values.append(val)
        return output 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Magic method/operator overload for exponentiation."""
        output: Simpy = Simpy([])
        if type(rhs) == float:
            for x in range(0, len(self.values)):
                val: float = self.values[x] ** rhs
                output.values.append(val)
        else:   # rhs is a Simpy
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                val: float = self.values[x] ** rhs.values[x]
                output.values.append (val)
        return output 

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Magic method/operator overload for equality."""
        output: list[bool] = []
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                if self.values [idx] == rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for idx in range (0, len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    output.append(True)
                else:  
                    output.append(False)
        return output

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Magic method/operator overload for greater than expression."""
        output: list[bool] = []
        if type(rhs) == float:
            for idx in range(0, len(self.values)):
                if self.values [idx] > rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for idx in range (0, len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    output.append(True)
                else:  
                    output.append(False)
        return output

    def __getitem__(self, rhs: int) -> float:
        """Magic method/operator overload for subscription notation."""
        if type(rhs) == int:
            return self.values[rhs]
        else:
            output: Simpy = Simpy([])
            for idx in range (0, len(rhs)):
                if rhs[idx] == True:
                    output.values.append(self.values[idx])
        return output