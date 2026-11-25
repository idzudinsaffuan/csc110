from typing import Any
class Stack:
    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self.items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items."""
        return self.items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack

        Precondition: not self.is_empty()
        """
        return self.items.pop()

from typing import Any


class Stack1:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in first-in, last-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack1()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: The items stored in the stack. The end of the list represents
    #     the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack.
        """
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        return self._items.pop()

class Stack2:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in first-in, last-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    >>> s = Stack2()
    >>> s.is_empty()
    True
    >>> s.push('hello')
    >>> s.is_empty()
    False
    >>> s.push('goodbye')
    >>> s.pop()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: The items stored in the stack. The FRONT of the list represents
    #     the top of the stack.
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack.
        """
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.
        """
        return self._items == []


    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack.
        """
        self._items.insert(0, item)


    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Preconditions:
            - not self.is_empty()
        """
        self._items.pop(0)


def is_balanced(line: str) -> bool:
    """Return whether <line> contains balanced parentheses.

    Ignore square and curly brackets.

    >>> is_balanced('(a * (3 + b))')
    True
    >>> is_balanced('(a * (3 + b]]')  # Note that the two ']'s don't matter.
    False
    >>> is_balanced('1 + 2(x - y)}')  # Note that the '}' doesn't matter.
    True
    >>> is_balanced('3 - (x')
    False
    """
    s = Stack()

    for c in line:
        if c == '(':
            s.push('(')
        elif c == ')':
            if s.is_empty():
                return False
            s.pop()

    return s.is_empty()

def size(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size(s)
    3
    """
    temp_stack = Stack()
    count = 0
    while not s.is_empty():
        temp_stack.push(s.pop())
        count += 1

    while not temp_stack.is_empty():
        s.push(temp_stack.pop())

    return count
