"""Defining a Class!"""

from __future__ import annotations

"""
Think of a class definition as "roadmap" for objects that belong to the class 
You are defining the underlying structure every instance of this class will have
"""



class Pizza:

    #attributes
    # think of these as the variable each instance of my class will have
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings = int, inp_gf = bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        # returns a Pizza object

    def price(self) -> float:
        """Method to Calculate price of pizza"""
        if self.size == "large":
        price: flaot = 6.25
        else:
            price: float = 5.00
        price += .75 * input_pizza.toppings
        if self.gluten_free:
            price: += 1.00
        return price

    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppins: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza