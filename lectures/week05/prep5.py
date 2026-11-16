"""CSC110 Fall 2026 Prep 5: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Implement the function so that it does what its description claims.

Do *not* add any new preconditions!

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to have!

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
# Do not modify the dataclass below
###############################################################################

@dataclass
class Person:
    """A person with some basic demographic information.
    """
    given_name: str
    family_name: str
    age: int
    address: str

###############################################################################
# Prep exercises start here
###############################################################################


@check_contracts
def greet_person(person: Person) -> str:
    """Return a greeting message for the given person.

    The message should have the form 'Hello, <given_name> <family_name>!'

    >>> bahar = Person('Bahar', 'Aameri', 110, '110 St. George Street')
    >>> greet_person(bahar)
    'Hello, Bahar Aameri!'
    """
    return 'Hello, ' + person.given_name + ' ' + person.family_name + '!'


@check_contracts
def older_name(p1: Person, p2: Person) -> str:
    """Return the first name of the person who is older among p1 and p2.

    If p1 and p2 have the same age, return the name of p1.

    >>> david = Person('David', 'Liu', 110, '110 St. George Street')
    >>> mario = Person('Mario', 'Badr', 111, '111 St. George Street')
    >>> older_name(david, mario)
    'Mario'
    """
    if p2.age > p1.age:
        return p2.given_name
    else:
        return p1.given_name


@check_contracts
def total_age(people: list[Person]) -> int:
    """Return the total age of the people in people.

    >>> sadia = Person('Sadia', 'Sharmin', 110, '110 St. George Street')
    >>> paul = Person('Paul', 'He', 111, '111 St. George Street')
    >>> example_people = [sadia, paul]
    >>> total_age(example_people)
    221
    """
    return sum([x.age for x in people])


@check_contracts
def any_has_name(people: list[Person], name: str) -> bool:
    """Return whether at least one given person has a given_name equal to name OR
    a family_name equal to name.

    Note: you must implement this function using a for loop, using the early return pattern.
    As a hint, the equivalent comprehension expression is:

        any({person.given_name == name or person.family_name == name for person in people})
    """
    for person in people:
        if name in {person.given_name, person.family_name}:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VS Code, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120
    })
