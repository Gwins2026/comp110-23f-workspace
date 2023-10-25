"""Combining two lists into a dictionary."""

__author__ = "730561330"


def zip(list_1: list[str]), list_2: list[int]) -> dict[str, int]:
    """Creates a dictionary with keys as strings from list_1 and values as integers from list_2."""
    if len(list_1) != len(list_2) or (len(list_1) == 0):
        return {}
    zips: dict[str, int] = {}
    i: int = 0
    while i < len(list_1):
        zips[list_1[i]] = list_2[i]
        i += 1
    return zips