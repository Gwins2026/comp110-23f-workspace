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
    color_counts: dict[str, str] = {}
    first_appearance: dict[str, str] = {}
    fav_color: str = None
    i: int = 0
    for name, color in colors.items():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
            first_appearance[color] = name
        if color_counts[color] > i:
            i = color_counts[color]
            fav_color = color
        elif color_counts[color] == i:
            if name == first_appearance[color]:
                fav_color = color
    return fav_color 


def count(freq_list: list[str]) -> dict[str, int]:
    """Given a list of strings, function produces a dictionary according to frequency of each value in input list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(freq_list):
        if freq_list[i] in result:
            result[i] += 1
            i += 1
        else:
            result() += {freq_list[i]: 1}
            i += 1
    return result 


def alphabetizer(cate_list: list[str]) -> dict[str, list[str]]:
    """Given a list of strings, function cataegorizes list into an order according to first letter in the string."""
    result: dict[str, list[str]] = {}
    cate_list.lower()
    i: int = 0
    while i < len(cate_list):
        if cate_list[i[0]] in result:
            result[cate_list[i[0]]] += cate_list[i]
        else:
            result() += {cate_list[i[0]]: cate_list[i]}
        i += 1
    return result 


def update_attendance(attend_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a dictionary of students and their class attendance, function updates and changes that dictionary to reflect new attendance by students."""
    for key in attend_log:
        if key == day:
            attend_log[key] += student
        else: 
            attend_log() += {day: student}
    return attend_log 