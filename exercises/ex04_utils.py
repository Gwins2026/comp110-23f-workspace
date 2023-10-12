"""EX04 - Utils."""

__author__ = "730561330"


def all(xs: list[int], guess: int) -> bool:
    """Determines whether a given list has all the same integers."""
    if len(xs) == 0
        return(False)
    i: int = 0
    while i <= len(xs) - 1:
        if xs[i] == guess:
            i += 1
        else:
            return(False)
    return(True)

def max(inputs: list[int]) -> int:
    """Returning the largest integer in a list."""
    if len(inputs) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_input: int = inputs[0]
    while i < len(inputs) - 1:
        if inputs[i] >= max_input:
            max_input = inputs[i]
        i += 1
    return(max_input)

def is_equal(x: list[int], y: list[int]) -> bool:
    """Determines if two lists are identical or not."""
    if len(x) != len(y):
        return(False)
    i: int = 0
    while i <= len(x) - 1:
        if x[i] == y[i]:
            i += 1
        else:
            return(False)
    return(True)