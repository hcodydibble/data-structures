"""A Doubly Linked List."""


class Node(object):
    """Create a Node object."""

    def __init__(self, data, next=None, previous=None):
        """Initialized values of the Node object."""
        self.data = data
        self.next = next
        self.previous = previous


class DLL(object):
    """Create a Doubly Linked List object."""

    def __init__(self):
        """Initialized values of the Doubly Linked List object."""
        self.head = None
        self.tail = None
        self._counter = 0

    def push(self, val):
        """Push a new value to the list."""
        old_head = self.head
        self.head = Node(val, next=self.head)
        self._counter += 1
        if old_head:
            old_head.previous = self.head
        else:
            self.tail = self.head

    def append(self, val):
        """Append a new value to the list."""
        old_tail = self.tail
        self.head = Node(val, previous=self.tail)
        self._counter += 1
        if old_tail:
            old_tail.next = self.tail
        else:
            self.head = self.tail
