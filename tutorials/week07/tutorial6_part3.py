"""CSC110 Tutorial 6: Loops and Mutation, Exercise 3

Module Description
==================
This module contains the function for you to implement for Exercise 3 of this tutorial.
The function you'll implement should closely follow the idea described in the handout.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""


###############################################################################
# Exercise 3
###############################################################################
def get_linear_combination(a: int, b: int, n: int) -> tuple[int, int]:
    """Return integers (p, q) such that a * p + b * q == n.

    Note: for given values of (a, b, n), there are infinitely many possible
    (p, q) that could be returned. You may return any pair of integers
    that satisfy the description.

    Preconditions:
        - math.gcd(a, b) == 1
        - a >= 1
        - b >= 1

    >>> p, q = get_linear_combination(10, 3, 6)
    >>> p * 10 + q * 3 == 6
    True
    """
    result = extended_euclidean_gcd(a ,b)
    return (n*result[1], n*result[2])



def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q.

    Preconditions:
    - a >= 0
    - b >= 0

    >>> extended_euclidean_gcd(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    # Initialize px, qx, py, and qy
    px, qx = 1, 0  # Since x == a == 1 * a + 0 * b
    py, qy = 0, 1  # Since y == b == 0 * a + 1 * b

    while y != 0:
        # assert math.gcd(a, b) == math.gcd(x, y)  # Loop Invariant 1
        assert x == px * a + qx * b                # Loop Invariant 2
        assert y == py * a + qy * b                # Loop Invariant 3

        q, r = divmod(x, y)  # quotient and remainder when x is divided by y

        # Update x and y
        x, y = y, r

        # Update px, qx, py, and qy
        px, qx, py, qy = py,  qy, px - q * py, qx - q * qy

    return x, px, qx


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
