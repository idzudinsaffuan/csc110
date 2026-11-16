"""CSC110 Fall 2026 Prep 3: Programming Exercises

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
# Reference functions; do NOT edit the two functions below
###############################################################################
def mystery_1_nested(x: int, y: set) -> str:
    if x > 0:
        if len(y) >= 1 and all({n > x for n in y}):
            return 'Pocoyo'
        else:
            return 'Tomoyo'
    else:
        return 'Pocoyo'



def mystery_2_if(x: int, y: set, z: set) -> bool:
    if x in y:
        if x not in y:
            return True
        elif x in z or x not in y:
            return False
        else:
            return True
    else:
        if x in z:
            return False
        else:
            return False


###############################################################################
# Complete the functions below as per the instructions/docstrings
###############################################################################

"""
Instructions for mystery_1_flat:

Rewrite the reference function mystery_1_nested below, so the body
consists of *just one single if statement block* (that is, one if statement
block containing exactly one `if` branch, possibly followed by multiple `elif`
branches and an `else` branch, but no other `if` branches nested within it).

All `return` statements in the function body should be contained within branches
of the if statement (including the `else` branch).

All boolean expressions should be simplified to remove redundant conditions
(e.g., `x > 1 and x > 0` can be simplified to `x > 1`).
"""

def mystery_1_flat(x: int, y: set) -> str:
    """Return the same value as mystery_1_nested above, but using just a
    single if statement.
    """

    if x > -1 and len(y) >= 1 and all({n > x for n in y}):
        return 'Pocoyo'
    elif x < -1 and len(y) <= 1 and all({n > x for n in y}):
        return 'Tomoyo'
    else:
        return 'Tomoyo'

"""
Instructions for mystery_2_no_if:

Rewrite the reference function mystery_2_if below so it performs the same computation,
but the body consists of NO if statements at all.

You may use local variables to save "intermediate values" in a larger boolean expression.

All boolean expressions should be simplified to remove redundant conditions
(e.g., `x > 1 and x > 0` can be simplified to `x > 1`).
"""
def mystery_2a_no_if(x: int, y: set, z: set) -> bool:
    """Return the same value as mystery_2a_if, but without using any if statements.
    """

    equal_x_for_z = {x == num for num in z}
    equal_x_for_y = {x == num for num in y}
    return any(equal_x_for_y) and not(any(equal_x_for_z))
