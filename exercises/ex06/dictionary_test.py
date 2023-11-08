"""EX07 - 'dict' Unit Tests."""

__author__ = "730561330"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


#  INVERT
def test_empty_invert():
    """Invert of empty dict should result in {}."""
    assert invert({}) == {}


def test_invert_reg():
    """Testing a dict of regular inputs to make sure the function invert runs properly."""
    input_dict: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    output_dict: dict[str, str] = {"b": "a", "d": "c", "f": "e"}
    assert invert(input_dict) == output_dict


def test_invert_mult_char():
    """Testing entries with multiple characters in a dict."""
    input_dict: dict[str, str] = {"pow": "bang", "can": "soup", "blah": "bored"}
    output_dict: dict[str, str] = {"bang": "pow", "soup": "can", "bored": "blah"}
    assert invert(input_dict) == output_dict


#  FAVORITE_COLOR
def test_empty_fav_color(): 
    """Favorite_color of empty dict should result in {}."""
    assert favorite_color({}) == {}


def test_fav_color_reg():
    """Testing a dict of regular inputs to make sure the function favorite_color runs properly."""
    test_dict: dict[str, str] = {"Bob": "green", "Jerry": "green", "Charles": "blue"}
    assert favorite_color(test_dict) == "green"


def test_multiple_fav_colors():
    """Testing a dict with multiple favorite colors."""
    test_dict: dict[str, str] = {"Johnny": "blue", "Suzzy": "purple", "Alex": "green", "Brandon": "purple", "Chloe": "green"}
    assert favorite_color(test_dict) == "purple"


#  COUNT
def test_empty_count():
    """Count of empty lists should result in {}."""
    assert count([]) == {}


def test_count_freq():
    """Testing a given list with strings that appear only once for the resulting dict frequency."""
    test_list: list[str] = ["random", "basketball", "find"]
    output_dict: dict[str, int] = {"random": 1, "basketball": 1, "find": 1}
    assert count(test_list) == output_dict


def test_count_reg():
    """Testing a list of regular inputs to make sure the function count runs properly."""
    test_list: list[str] = ["a", "b", "c", "a", "b", "a"]
    output_dict: dict[str, int] = {"a": 3, "b": 2, "c": 1}
    assert count(test_list) == output_dict


#  ALPHABETIZER
def test_empty_alphabetizer():
    """Alphabetizer of empty list should result in {}."""
    assert alphabetizer([]) == {}


def test_alphabetizer_reg():
    """Testing a list of regular inputs to make sure the function alphabetizer runs properly."""
    test_list: list[str] = ["apple", "pear", "grape", "blueberry"]
    output_dict: dict[str, list[str]] = {"a": ["apple"], "p": ["pear"], "g": ["grape"], "b": ["blueberry"]}
    assert alphabetizer(test_list) == output_dict


def test_alphabetizer_mult_words():
    """Tests a list of mutiple words with the same first letter."""
    test_list: list[str] = ["apple", "animal", "amazing", "bat", "boardgame", "barbie", "fire", "fart"]
    output_dict: dict[str, list[str]] = {"a": ["apple", "animal", "amazing"], "b": ["bat", "boardgame", "barbe"], "f": ["fire", "fart"]}
    assert alphabetizer(test_list) == output_dict


#  UPDATE_ATTENDANCE
def test_already_update_attendance():
    """Testing on a list that already accounts for the given student on that day."""
    input_dict: dict[str, list[str]] = {"monday": ["Sarah", "Johnny"], "tuesday": ["Johnny"], "wednesday": ["Jenny", "Sarah"]}
    test_day: str = "tuesday"
    test_student: str = "Brad"
    assert update_attendance(input_dict, test_day, test_student) == input_dict


def test_update_attendance_reg():
    """Testing a dict of regular inputs to make sure the function update_attendance runs properly."""
    input_dict: dict[str, list[str]] = {"monday": ["Sarah", "Johnny"], "tuesday": ["Johnny"], "wednesday": ["Jenny", "Sarah"]}
    test_day: str = "wednesday"
    test_student: str = "Jenny"
    output_dict: dict[str, list[str]] = {}
    assert update_attendance(input_dict, test_day, test_student) == output_dict


def test_empty_attendance():
    """Testing an empty attendance dict when adding a new day and student to it."""
    input_dict: dict[str, list[str]] = {}
    test_day: str = "thrusday"
    test_student: str = "Monica"
    output_dict: dict[str, list[str]] = {"thursday": ["Monica"]}
    assert update_attendance(input_dict, test_day, test_student) == output_dict