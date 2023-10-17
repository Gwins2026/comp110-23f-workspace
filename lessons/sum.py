"""Summing the elements of a list using different loops."""
__author__ = "730561330"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements in a list."""
    i: int = 0
    sums: float = 0.0
    while i < len(vals):
        sums += vals[i]
        i += 1
    return sums 


def f_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in a list."""
    sums: float = 0.0
    for elem in vals:
        sums += elem
    return sums 


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in a list."""
    sums: float = 0.0
    for idx in range(0, len(vals)):
        sums += vals[idx]
    return sums 


# class notes
    pets: list[str] = ["Louie", "Bo", "Bear"]
for idx in pets:
   print(f"Good boy, {idx}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
   elem: str = names[idx]
   print(f"{idx}: {elem}")