"""CSC110 Tutorial 2: Functions, Logic, and Autocorrecting with Predicates (Exercise 3)

Module Description
==================
This module contains the (incorrectly implemented) functions for Exercise 3
and skeletons of unit tests for each function. The bottom of this file includes
the boilerplate code for running the unit tests using pytest. To run the tests,
right-click and select "Run File in Python Console".

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


###############################################################################
# max_even
###############################################################################
def max_even(numbers: list) -> int:
    """Return the largest even number in the list.

    If there are no even numbers, return 0.
    """
    return max([number for number in numbers if number % 2 == 0])


def test_max_even_passing() -> None:
    """Test max_even with a set of number
    """
    actual = max_even([1,2,3,4,5,6,7,8])
    expected = 8
    assert expected == actual


def test_max_even_failing() -> None:
    """Test max_even with a set of number
    """


###############################################################################
# max_corresponding_value
###############################################################################
def max_corresponding_value(map1: dict, map2: dict, key: str) -> int:
    """Compare the values corresponding to key in map1 and map2, and return the larger value.

    If key is only in one of the dicts, return its corresponding value in that dict.
    If key is in neither dict, return 0.

    You may ASSUME that:
        - map1 and map2 both map strings to integers
    """
    if key in map1:
        return map1[key]
    elif key in map2:
        return map2[key]
    elif key in map1 and key in map2:
        return max(map1[key], map2[key])
    else:  # the key is in neither dictionary
        return 0


def test_max_corresponding_value_passing() -> None:
    """Test max_corresponding_value with ___________

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and PASSES.
    """


def test_max_corresponding_value_failing() -> None:
    """Test max_corresponding_value with ___________

    TODO: complete this test (description and body) so that it calls max_corresponding_value
          and FAILS.
    """


if __name__ == '__main__':
    import pytest
    pytest.main(['tutorials/week02/tutorial2_ex3.py', '-v'])
