"""CSC110 Tutorial 3: Function Correctness and Property-Based Testing (Exercise 3)

Module Description
==================
Write your property-based tests for Exercise 3 in this file.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
import math  # Imported so you can use math.gcd in your tests

from hypothesis import given
from hypothesis.strategies import integers


# A divisibility predicate that includes 0.
# Useful for property (d).
def divides(d: int, n: int) -> bool:
    """Return whether d divides n."""
    if d == 0:
        return n == 0
    else:
        return n % d == 0


@given(m=integers(), n=integers())
def test_a(m: int, n: int) -> None:
    """Test that m is zero and n is zero or greatest common divisor of m and n is greater than or equal to 1"""
    assert (m == 0 and n == 0) or math.gcd(m, n) >= 1

@given(n=integers())
def test_b(n: int) -> None:
    """Test that the greatest common divisor of n and 0 is the absolute value of n"""
    assert math.gcd(n, 0) == abs(n)

@given(m=integers(), n=integers())
def test_c(m: int, n: int) -> None:
    """Test that the greatest common divisor of 2m and 2n is 2 times the greatest common divisor of m and n"""
    assert math.gcd(2 * m, 2 * n) == 2 * math.gcd(m, n)

@given(d=integers(), n=integers())
def test_d(d: int, n: int) -> None:
    """test that d divides n implies the greatest common divisor of d an n is equal to the absolute value of d"""
    assert (not divides(d,n)) or (math.gcd(d,n) == abs(d))

# In the space below, you should write tests for the other three properties on
# the tutorial handout. You can (and should) copy the same structure as test_a.


if __name__ == '__main__':
    import pytest
    pytest.main(['tutorials/week04/tutorial3_part3.py', '-v'])
