from dll import DLL


class Deque(object):
    """Create a Deque object."""

    def __init__(self):
        """The init values of the Deque object."""
        self._dll = DLL()

    def append(self, val):
        """Add a node to the back of the Deque."""
        self._dll.append(val)

    def appendleft(self, val):
        """Add a node to the front of the Deque."""
        self._dll.push(val)

    def pop(self):
        """Remove node from the back of the Deque."""
        try:
            return self._dll.shift()
        except IndexError:
            raise IndexError('Nothing in the Deque')

    def popleft(self):
        """Remove a node from the front of the Deque."""
        try:
            return self._dll.pop()
        except IndexError:
            raise IndexError('Nothing in the Deque')

    def peek(self):
        """Get value of the next Node to be popped from the left."""
        if self._dll._counter == 0:
            return None
        return self._dll.tail.data

    def peekleft(self):
        """Get value of the next Node to be popped from the right."""
        if self._dll._counter == 0:
            return None
        return self._dll.head.data

    def size(self):
        """Return the size of the Deque."""
        return self._dll._counter
