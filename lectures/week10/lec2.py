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

class Queue:
    items : list
    def __init__(self):
        """Initialize an empty Queue"""
        self.items = []
    def enqueue(self, item: Any) -> None:
        """Add an item to the queue"""
        self.items.append(item)
    def dequeue(self) -> Any:
        """Remove an item from the front of the queue"""
        return self.items.pop(0)



from typing import Any


class PriorityQueueUnsorted:
    """A queue of items that can be dequeued in priority order.

    When removing an item from the queue, the highest-priority item is the one
    that is removed.

    >>> pq = PriorityQueueUnsorted()
    >>> pq.is_empty()
    True
    >>> pq.enqueue(1, 'hello')
    >>> pq.is_empty()
    False
    >>> pq.enqueue(5, 'goodbye')
    >>> pq.enqueue(2, 'hi')
    >>> pq.dequeue()
    'goodbye'
    """
    # Private Instance Attributes:
    #   - _items: A list of the items in this priority queue.
    #             Each element is a 2-element tuple where the first element is
    #             the priority and the second is the item.

    _items: list[tuple[int, Any]]

    def __init__(self) -> None:
        """Initialize a new and empty priority queue."""
        self._items = []


    def is_empty(self) -> bool:
        """Return whether this priority queue contains no items.
        """
        return self._items == []


    def enqueue(self, priority: int, item: Any) -> None:
        """Add the given item with the given priority to this priority queue.
        """
        self._items.append((priority,item))


    def dequeue(self) -> Any:
        """Remove and return the element of this priority queue with the highest priority.

        Preconditions:
            - not self.is_empty()
        """
        index_of_highest = 0
        highest_so_far = self._items[index_of_highest][0]

        for i in range(1, len(self._items)):
            if self._items[i][0] > highest_so_far:
                highest_so_far = self._items[i][0]
                index_of_highest = i
        
        item = self._items.pop(index_of_highest)
        return item[1]
