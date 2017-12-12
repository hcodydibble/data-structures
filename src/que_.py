"""Make a Queue object that has access to DoublyLinkedList methods."""
from dll import DLL


class Queue(object):
    """Create a Queue object."""

    def __init__(self):
        """Initialize Queue using DLL methods."""
        self._dll = DLL()

    def enqueue(self, val):
        """Add a node to queue."""
        self._dll.push(val)

    def dequeue(self):
        """Remove first node pushed in."""
        try:
            return self._dll.shift()
        except IndexError:
            raise IndexError('Nothing to dequeue')