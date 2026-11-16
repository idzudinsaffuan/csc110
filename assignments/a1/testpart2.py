def pixelate_row(colour_row: list, size: int) -> list:
    """Return a pixelated version of the row with a "digicam" filter applied,
    which looks like the effect from some digital cameras.

    In the digicam filter, size pixels are grouped together and replaced with
    pixels of a single color, where the individual red, green, and blue
    components are the average of the corresponding components for every pixel
    in the group, rounded down to the nearest integer. This is repeated for
    all the colours in the row.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB sublists)
    - size > 0
    - len(colour_row) can be divided evenly by size

    >>> pixelate_row([[0, 1, 3]], 1)
    [[0, 1, 3]]
    >>> pixelate_row([[0, 1, 3], [3, 3, 3]], 2)
    [[1, 2, 3], [1, 2, 3]]
    >>> example_colour = [[0, 0, 0], [255, 255, 255], [0, 0, 255], [67, 67, 67], [255, 0, 0], [100, 0, 100]]
    >>> pixelate_row(example_colour, 2)
    [[127, 127, 127], [127, 127, 127], [33, 33, 161], [33, 33, 161], [177, 0, 50], [177, 0, 50]]

    HINT: consider designing one or more helper functions. Think about what
    operations this function will need to perform repeatedly!
    """
    grouped = [[colour_row[x] for x in range(y * size, (y+1) * size)] for y in range (0,len(colour_row)//size)]
    combined = [average_colour(group) for group in grouped]
    return sum(combined, [])




def average_colour(colour_row: list) -> list:
    """
    Return the average value of R, G and B in the corresponding list of colours.

    >>> average_colour([[10, 20, 30], [40, 50, 60]])
    [[25, 35, 45], [25, 35, 45]]
    >>> average_colour([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    [[40, 50, 60], [40, 50, 60], [40, 50, 60]]
    """
    averaged = [sum([colour[0] for colour in colour_row]) // len(colour_row)] + \
    [sum([colour[1] for colour in colour_row]) // len(colour_row)] + \
    [sum([colour[2] for colour in colour_row]) // len(colour_row)]

    return [averaged] * len(colour_row)

example_colour = [[0, 0, 0], [255, 255, 255], [0, 0, 255], [67, 67, 67], [255, 0, 0], [100, 0, 100]]
print(pixelate_row(example_colour, 2))
