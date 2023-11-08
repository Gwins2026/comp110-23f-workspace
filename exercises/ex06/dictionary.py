"""EX06 - Practice using Dictionary Functions."""

__author__ = "730561330"


def invert(dicts: dict[str, str]) -> dict[str, str]:
    """A given dictionary is inverted and the key list becomes the values of the output list and vice versa."""
    inverted: dict[str, str] = {}
    for key, value in dicts.items():
        if value in inverted:
            raise KeyError("A given list value repeats itself.")
        inverted[value] = key
    return inverted 


def favorite_color(colors: dict[str, str]) -> str:
    """In a given dictionary of people and their favorite color, function determines which color is most popular."""
    # Creates new dictionary
    color_counts: dict[str, int] = {}
    for key in colors:
        if colors[key] in color_counts:
            color_counts[colors[key]] += 1
        else:   # New color encontered
            color_counts[colors[key]] = 1
    maxs: int = 0
    fav: str = ""
    for key in color_counts:
        # Checks color's count values against the curren max, and assigns the color to the overall favorite if greater
        if color_counts[key] > maxs:
            maxs = color_count[key]
            # Assigns the color to the overall favorite if greater
            colors = key
    return colors


def count(freq_list: list[str]) -> dict[str, int]:
    """Given a list of strings, function produces a dictionary according to frequency of each value in input list."""
    result: dict[str, int] = {}
    for key in freq_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result 


def alphabetizer(cate_list: list[str]) -> dict[str, list[str]]:
    """Given a list of strings, function cataegorizes list into an order according to first letter in the string."""
    result: dict[str, list[str]] = {}
    for key in cate_list:
        first_letter = key[0].lower()
        if first_letter in result:
            result[first_letter].append(key)
        else:
            result[first_letter] = [key]
    return result 


def update_attendance(attend_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a dictionary of students and their class attendance, function updates and changes that dictionary to reflect new attendance by students."""
    new_log: dict[str, list[str]] = current_log
    if day in new_log:
        if student in new_log[day]:
            return current_log
        else: # Adds student to day's attendance
            new_log[day].append[student]
    else: # Selected day's attendance is not yet present
        new_log[day] = [student]
    return attend_log 