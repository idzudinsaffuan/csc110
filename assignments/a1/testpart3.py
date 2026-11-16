def average_colour(colour_row: list) -> list:
    """
    Return the list of the averaged values of R, G and B in the corresponding list of colours.

    >>> average_colour([[10, 20, 30], [40, 50, 60]])
    [[25, 35, 45], [25, 35, 45]]
    >>> average_colour([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    [[40, 50, 60], [40, 50, 60], [40, 50, 60]]
    """
    averaged = [sum([colour[0] for colour in colour_row]) // len(colour_row)] + \
        [sum([colour[1] for colour in colour_row]) // len(colour_row)] + \
        [sum([colour[2] for colour in colour_row]) // len(colour_row)]

    return averaged
