"""CSC110 Tutorial 9: Running-Time Analysis, Exercise 3

Module Description
==================
This module contains function headers you should implement for finding the
convex hull of a set of points. A function that animates the convex hull
one line at a time is also provided in tutorial9_part3_animated.py.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
import math

from python_ta.contracts import check_contracts


@check_contracts
def convex_hull(points: set[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return the convex hull of the given points.

    The first point in the convex hull is the one with the smallest x-coordinate,
    breaking ties by picking the point with the smallest y-coordinate.
    The points in the convex hull appear in clockwise order.

    Preconditions:
        - len(points) >= 3

    >>> example_points = ...
    >>> convex_hull(example_points)
    (Write the expected output here)
    """


@check_contracts
def leftmost(points: set[tuple[int, int]]) -> tuple[int, int]:
    """Return the leftmost (smallest x-coordinate) point in points.

    If there is a tie, return the one with the smallest y-coordinate.

    Note: because we're using pygame's coordinate system here, small y-coordinates
    translate to *higher* points in the visualization window.

    Preconditions:
        - points != set()
    """


@check_contracts
def angle_between(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> float:
    """Return the angle between line segments ab and ac, in radians.

    Preconditions:
        - b != a
        - c != a

    Hint: The `math` module has a function that you need!

    >>> result = angle_between((150, 350), (150, 351), (200, 100))
    >>> math.isclose(result, 2.9441970937399122)
    True

    Note: to avoid rounding error, you should use min and max to make sure
    your "cos" values are between -1 and 1.
    """


@check_contracts
def next_point(prev: tuple[int, int], curr: tuple[int, int], points: set[tuple[int, int]]) -> tuple[int, int]:
    """Return the next point in the convex hull after curr and prev.

    If there is a tie in the angle calculation, pick the point that is *furthest* away from curr.

    Preconditions:
      - len(points) >= 3
      - curr in points
      - curr and prev are both in the convex hull of points

    Implementation notes:
        - Call angle_between, but make sure you are passing in the arguments in the correct order
        - curr is in points; you need to skip over this point to ensure you don't violate a
          precondition for angle_between

    >>> pts = {(200, 100), (250, 200), (500, 300), (425, 100), (150, 350), (700, 30), (500, 500)}
    >>> next_point((150, 351), (150, 350), pts)
    (200, 100)
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
