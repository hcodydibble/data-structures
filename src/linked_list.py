"""A Linked List object."""


class Node(object):
    """A node object."""

    def __init__(self, data, nxt=None):
        """The init values of a Node object."""
        self.data = data
        self.nxt = nxt


class LinkedList(object):
    """A Linked List object."""

    def __init__(self, iterable=None):
        """The init values of a Linked List object."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add a new Node containing the given value."""
        new_head = Node(val, nxt=self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remove and return the head Node and return it's value."""
        if not self.head:
            raise IndexError("The list is empty.")
        output = self.head.data
        self.head = self.head.nxt
        self._counter -= 1
        return output

    def size(self):
        """Return the size of the Linked List."""
        return self._counter

    def search(self, val):
        """Return the Node containing the given value."""
        curr = self.head
        while curr:
            if val == curr.data:
                return curr
            curr = curr.nxt
        return None

    def remove(self, node):
        """Remove the Node containing the given value."""
        if not self.head:
            raise IndexError("The list is empty.")
        if self.head == node:
            self.head = self.head.nxt
            self._counter -= 1
            return
        curr = self.head
        while curr.nxt:
            if curr.nxt == node:
                curr.nxt = node.nxt
                self._counter -= 1
                return
            curr = curr.nxt

    def display(self):
        """Display the Linked List."""
        curr = self.head
        output = []
        while curr:
            output.append(curr.data)
            curr = curr.nxt
        return tuple(output).__str__()

    def __len__(self):
        """Overwrite default return for the len function."""
        return self._counter

    def __str__(self):
        """Overwrite default return for the print function."""
        return self.display()
