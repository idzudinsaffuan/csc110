from typing import Any
class Stack:
    items : list
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

        Raise EmptyStackError if pop is called on an empty stack
        """
        if self.is_empty:
           raise EmptyStackError

        return self.items.pop()

class EmptyStackError(Exception):
    """Exception raised when calling pop on an empty stack"""
    def __str__(self):
        return 'pop an empty stack'
