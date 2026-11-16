"""CSC110 Fall 2026 Assignment 1, Part 2: Colour Rows

Instructions (READ THIS FIRST!)
===============================

Please follow the instructions in the assignment handout to complete this file.

Note that you only need to complete the function bodies.
You are not required to add more doctest examples, though you may do so to help
with your own understanding/testing.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""

import a1_helpers


###################################################################################################
# 0. Warmup
###################################################################################################
def warmup1() -> None:
    """Visualize an example colour row using pygame.

    This function illustrates the use of the helper function a1_helpers.show_colours_pygame
    that we have provided you. We encourage you to use that function to visualize your
    work on the various questions in this part of the assignment!
    """
    example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    a1_helpers.show_colours_pygame(example_colours)

###################################################################################################
# 1. Cropping colour rows
###################################################################################################


def crop_row(colour_row: list, start: int, num_colours: int) -> list:
    """Return a colour row containing the specified colours from the given colour_row.

    Notes:
    1. start is the index of the first colour to take from colour_row.
    2. num_colours specifies the number of colours to take from colour_row.
        If num_colours == 0, no colours are taken (and an empty list is returned)

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB sublists)
    - start >= 0
    - num_colours >= 0
    - start + num_colours <= len(colour_row)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row(example_colours, 1, 2)  # Take two colours from example_colours starting at index 1
    [[1, 2, 3], [100, 100, 100]]
    """
    return [colour_row[x] for x in range(start, start + num_colours)]


def crop_row_border_multiple(colour_row: list, border_size: int) -> list:
    """Return a colour row with the colours from the given colour_row, except with
    the first and last border_size colours removed.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB sublists)
    - 1 <= border_size <= len(colour_row) // 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row_border_multiple(example_colours, 1)  # Remove the first and last colours
    [[1, 2, 3], [100, 100, 100], [181, 57, 173]]
    >>> crop_row_border_multiple(example_colours, 2)  # Remove the first 2 and last 2 colours
    [[100, 100, 100]]

    You may implement this function by using a list comprehension OR by calling crop_row
    with the appropriate arguments. (For extra practice, try both ways!)
    """
    return [colour_row[x] for x in range(border_size, len(colour_row) - border_size)]


###################################################################################################
# 2. Changing colours
###################################################################################################
def remove_red_in_row(colour_row: list) -> list:
    """Return a new colour row consisting of the same colours as the given row, except each colour
    has its "red" value changed to 0.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB sublists)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> remove_red_in_row(example_colours)
    [[0, 255, 200], [0, 2, 3], [0, 100, 100], [0, 57, 173], [0, 0, 197]]
    """
    return [[0] + [colour[1]] + [colour[2]] for colour in colour_row]


def greyscale(colour_row: list) -> list:
    """
    Return a new colour row consisting of the *grayscale version* of each
    colour in the given row.

    The grayscale version of a colour [r, g, b] is equal to [x, x, x], where
    x is the average of r, g, and b, rounded down to the nearest integer.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB sublists)

    >>> example_colours = [[100, 100, 100], [200, 100, 0], [25, 30, 20]]
    >>> greyscale(example_colours)
    [[100, 100, 100], [100, 100, 100], [25, 25, 25]]
    """
    return [3 * [sum(colour) // 3] for colour in colour_row]

###################################################################################################
# 3. Distorting colours
###################################################################################################


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
    grouped = [[colour_row[x] for x in range(n * size, (n + 1) * size)] for n in range(0, len(colour_row) // size)]
    averaged_grouped = ([average_colour(group) for group in grouped])
    return sum(averaged_grouped, [])


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

    return [averaged] * len(colour_row)


###################################################################################################
# "Main block" (we'll discuss what this means in lecture)
###################################################################################################
if __name__ == '__main__':
    # The following lines run all doctests in this file when you run the file.
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VSCode, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    #
    python_ta.check_all(config={
        'extra-imports': ['a1_helpers'],
        'max-line-length': 120,
        'disallowed-python-syntax': ['For', 'While', 'Slice']
    })
