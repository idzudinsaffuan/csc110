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
            s.pop('(')

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
