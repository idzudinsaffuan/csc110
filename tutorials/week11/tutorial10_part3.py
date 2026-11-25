"""CSC110 Tutorial 10: Running-Time Analysis and Abstract Data Types, Exercise 3

Module Description
==================
This module contains the ListMap class that you must complete to be a
concrete definition of the Mapping ADT.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""
from typing import Any


class ListMap:
    """An implementation of the Mapping ADT using a list."""
    # Private Instance Attributes:
    #   - _pairs: A list of tuples, where each tuple stores a (key, value) pair
    #             in the mapping.
    _pairs: list[tuple[Any, Any]]

    def __init__(self) -> None:
        """Initialize a new empty mapping."""

    def size(self) -> int:
        """Return the number of key-value pairs in this mapping."""

    def assign(self, key: Any, new_value: Any) -> None:
        """Assign the given key to the given value in this mapping.

        The given value replaces any existing corresponding value if the key was
        already in this mapping.
        """

    def lookup(self, key: Any) -> Any:
        """Look up the corresponding value for this key in this mapping.

        Raise a KeyError if key is not in this mapping.

        >>> m = ListMap()
        >>> m.assign('a', 1)
        >>> m.assign('b', 2)
        >>> m.assign('c', 3)
        >>> m.lookup('b')
        2
        """

    def pop(self, key: Any) -> Any:
        """Remove and return the corresponding value of the given key from this mapping.

        Raise a KeyError if key is not in this mapping.

        >>> m = ListMap()
        >>> m.assign('a', 1)
        >>> m.assign('b', 2)
        >>> m.assign('c', 3)
        >>> m.pop('b')
        2
        >>> m.size()
        2
        """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
