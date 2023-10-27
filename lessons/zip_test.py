"""Test my zip function."""

__author__ = "730561330"

from lessons.zip import zip


def test_multiple_char():
    """Tests entries with multiple characters in the lists."""
    test_list_1: list[str] = ["shhh", "bang", "g"]
    test_list_2: list[int] = [5, 116, 88]
    assert zip(test_list_1, test_list_2) == {"shhh": 5, "bang": 116, "g": 88}


def test_empty_list():
    """Tests if when the list unequal list lengths are given, the zipped product produces an error."""
    test_list_1: list[str] = ["g", "e", "o"]
    test_list_2: list[int] = [1, 6]
    assert zip(test_list_1, test_list_2) == {}


def test_neg():
    """Tests negatives in the integer list."""
    test_list_1: list[str] = ["b", "a", "g"]
    test_list_2: list[int] = [-1, -2, -3]
    assert zip(test_list_1, test_list_2) == {"b": -1, "a": -2, "g": -3}