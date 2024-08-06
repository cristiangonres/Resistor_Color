"""Each resistor has a resistance value."""

def color_code(color : str) -> dict:
    """to look up the numerical value associated with a particular color band.

    :param color: str - color.
    :return: palete[color]: int - Value of color.
    """
    
    palete = {"black" :  0, "brown": 1, "red" :  2, "orange": 3, "yellow" :  4, "green": 5, "blue" :  6, "violet": 7, "grey" :  8, "white": 9}
    return palete[color]


def colors():
    """to list the different band colors.
    
    :return: colors: list - list the different band colors.
    """
    colors = [ "black", "brown","red","orange", "yellow", "green", "blue", "violet", "grey", "white" ]
    return colors
