"""CSC110 Fall 2026 Assignment 1, Part 1: Interpreting Test Results

Instructions (READ THIS FIRST!)
===============================

This Python module contains the program and tests described in Assignment 1,
Part 1. You can run this file as given to see the pytest report given in the
handout. Your task is to fix all errors in this file so that each test passes
(see problem set handout for details).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""

import pytest


def summarize_brightness_scores(colour_groups: dict) -> dict:
    """Return a mapping from colour group names to their total brightness scores.

    Each value in colour_groups is itself a list of RGB colours.

    See assignment handout for details.

    You may ASSUME that:
        - colour_groups is non-empty
        - every key in colour_groups is a str
        - every associated value in colour_groups is a non-empty list
        - every element of each list is an RGB colour
    """
    return {group: calculate_total_brightness_score(colour_groups[group])
            for group in colour_groups}


def calculate_total_brightness_score(colours: list) -> float:
    """Return the total brightness score of the given list of RGB colours.

    The brightness score of one RGB colour [r, g, b] is defined as:
        0.2126 * r + 0.7152 * g + 0.0722 * b

    You may ASSUME that:
        - colours is a non-empty list of RGB colours
    """
    total = sum([0.2126 * colour[0] + 0.7152 * colour[1] + 0.0722 * colour[2]
                 for colour in colours])

    return total


###############################################################################
# Unit Tests
###############################################################################
def test_calculation_one_group_one_colour() -> None:
    """Test summarize_brightness_scores with one group containing one colour."""
    colour_groups = {'living room': [[10, 20, 30]]}

    # DO NOT MODIFY ANY OF THE BELOW LINES IN THIS TEST
    expected = 18.596
    actual = summarize_brightness_scores(colour_groups)
    assert actual['living room'] == pytest.approx(expected)


def test_calculation_many_groups_same_colours() -> None:
    """Test summarize_brightness_scores with many groups that use the same
    colours.
    """
    same_colours = [[0, 0, 0], [10, 20, 30], [100, 100, 100]]
    colour_groups = {
        'living room': same_colours,
        'kitchen': same_colours,
        'bedroom': same_colours,
        'office': same_colours,
    }

    # DO NOT MODIFY ANY OF THE BELOW LINES IN THIS TEST
    expected = 118.596
    actual = summarize_brightness_scores(colour_groups)

    assert actual['living room'] == pytest.approx(expected)
    assert actual['kitchen'] == pytest.approx(expected)
    assert actual['bedroom'] == pytest.approx(expected)
    assert actual['office'] == pytest.approx(expected)


def test_calculation_many_groups_different_colours() -> None:
    """Test summarize_brightness_scores with many groups that use different
    colours.
    """
    colour_groups = {
        'living room': [[30, 80, 120], [150, 60, 20], [90, 90, 90]],
        'kitchen': [[255, 255, 255], [200, 150, 100], [50, 75, 125]],
        'bedroom': [[100, 40, 180], [20, 200, 60], [0, 0, 255]],
        'office': [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
    }

    # DO NOT MODIFY ANY OF THE BELOW LINES IN THIS TEST
    actual = summarize_brightness_scores(colour_groups)

    expected = 238.504
    assert actual['living room'] == pytest.approx(expected)

    expected = 485.315
    assert actual['kitchen'] == pytest.approx(expected)

    expected = 232.899
    assert actual['bedroom'] == pytest.approx(expected)

    expected = 145.788
    assert actual['office'] == pytest.approx(expected)


if __name__ == "__main__":
    pytest.main(['assignments/a1/a1_part1.py', '-v'])
