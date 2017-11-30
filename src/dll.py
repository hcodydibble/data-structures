"""A Doubly Linked List."""


class Node(object):
    """Create a Node object."""

    def __init__(self, data, nxt=None, prev=None):
        """Initialized values of the Node object."""
        self.data = data
        self.nxt = nxt
        self.prev = prev


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
        self.head = Node(val, nxt=self.head)
        self._counter += 1
        if old_head:
            old_head.prev = self.head
        else:
            self.tail = self.head

    def append(self, val):
        """Append a new value to the list."""
        old_tail = self.tail
        self.tail = Node(val, prev=self.tail)
        self._counter += 1
        if old_tail:
            old_tail.nxt = self.tail
        else:
            self.head = self.tail

    def pop(self):
        """Remove the head Node and return its value."""
        if len(self) == 0:
            self.head = None
            self.tail = None
        if not self.head:
            raise IndexError("There is nothing to pop.")
        output = self.head.data
        self.head = self.head.nxt
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._counter -= 1
        return output

    def shift(self):
        """Remove the tail Node and return its value."""
        if len(self) == 0:
            self.head = None
            self.tail = None
        if not self.tail:
            raise IndexError("There is nothing to shift.")
        output = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.nxt = None
        else:
            self.head = None
        self._counter -= 1
        return output

    def remove(self, val):
        """Remove the Node containing the given value."""
        if not self.head:
            raise IndexError("There is nothing in the list.")
        if self.head.data == val:
            self.pop()
            return
        curr = self.head
        while curr.nxt:
            if curr.data == val:
                curr.prev.nxt = curr.nxt
                curr.nxt.prev = curr.prev
                self._counter -= 1
                return
            curr = curr.nxt
        if val == self.tail.data:
            self.shift()
            return
        raise ValueError("No such Node in the list.")

    def _size(self):
        """Function to make __len__ work."""
        return self._counter

    def __len__(self):
        """Return length of our list."""
        return self._size()
