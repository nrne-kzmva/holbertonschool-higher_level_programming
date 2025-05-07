#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats. If the arguments are floats,
    they are casted to integers before the addition.
    Args:
        a (int, float): The first number.
        b (int, float): The second number, defaults to 98.
    Returns:
        int: The sum of a and b after casting them to integers if needed.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
