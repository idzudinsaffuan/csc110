"""CSC110 Fall 2026 Prep 6: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Implement the function so that it does what its description claims,
   using a for loop (NOT comprehensions -- or you can do both, for practice, if applicable).

    - You may use augmented assignment operations like "x += y" as a short form for
      "x = x + y".

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
from dataclasses import dataclass
from python_ta.contracts import check_contracts


###############################################################################
# This data class is the same one we used last week. Do NOT modify this part.
###############################################################################
@check_contracts
@dataclass
class Person:
    """A person with some basic demographic information.
    """
    given_name: str
    family_name: str
    age: int
    address: str


###############################################################################
# Exercises start here
###############################################################################
@check_contracts
def count_matching_ages(group1: list[Person], group2: list[Person]) -> int:
    """Return the number of *corresponding pairs of people*, one from group1 and one from group2,
    that have the same age.

    By "corresponding pair of people", we mean a person from group1 and a person from group2 with
    the same index. For example, group1[0] is compared with group2[0], group1[1] is compared with
    group2[1], etc.

    Preconditions:
    - len(group1) == len(group2)

    Note: you must implement this function using an INDEX-BASED for loop. This function is
    similar to the "Two lists, one loop" example in Section 5.6 of the Course Notes.
    """
    sum_so_far = 0
    for i in group1:
        for j in group2:
            if group2[j].age == group1[i].age:
                sum_so_far += 1
    return sum_so_far



####################################################################################################
# Mutation practice
####################################################################################################
def only_evens(lst: list[list[int]]) -> list[list[int]]:
    """Return a new list of the lists in lst that contain only even integers.

    Use a for loop with a list accumulator, and use mutating operations to update
    the accumulator in the loop body.

    >>> only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])
    [[4, 0, 6], [2]]
    """
    list_so_far = []
    for i in lst:
        if all([j % 2 == 0 for j in i]):
            [list_so_far] = [list_so_far + [i]]
    return list_so_far




def get_order_quantities(table_orders: dict[str, list[str]]) -> dict[str, int]:
    """Return a mapping from food item to the number of that item ordered.

    In the input dictionary table_orders:
        - Each key is the name of a person.
        - Each corresponding value is a list of the food items that person has ordered.
          Duplicates are allowed!

    In the returned dictionary:
        - Each key a a food item.
        - Each corresponding value is the number of times that food item was ordered
          in table_orders, across all people.

    Use a for loop with a dictionary accumulator, and use mutating operations to update
    the accumulator in the loop body.

    >>> orders = {'David': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],\
                  'Mario': ['Steak pie', 'Poutine', 'Vegetarian stew'],\
                  'Jen': ['Steak pie', 'Steak pie']}
    >>> get_order_quantities(orders) == {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}
    True
    """
    # TODO: complete this function body


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VS Code, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1714']
    })
