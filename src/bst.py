"""A Binary Search Tree!"""


class Node(object):
    """A node object."""

    def __init__(self, val, left_leaf=None, right_leaf=None):
        self.val = val
        self.left_leaf = left_leaf
        self.right_leaf = right_leaf
        self.depth = 0


class Tree(object):
    """A Binary Search Tree."""

    def __init__(self, iterable=None):
        self._root = None
        self.left_depth = 0
        self.right_depth = 0
        self._size = 0
        if isinstance(iterable, (list, tuple)):
            [self.insert(item) for item in iterable]

    def insert(self, val):
        """Insert a new node into the Tree containing the given value."""
        new_node = Node(val)
        if self._root is None:
            self._root = new_node
            self._size += 1
            return
        curr = self._root
        while curr:
            if new_node.val > curr.val:
                if curr.right_leaf is None:
                    curr.right_leaf = new_node
                    curr.right_leaf.depth = curr.depth + 1
                    if curr.right_leaf.depth > self.right_depth:
                        self.right_depth += 1
                    break
                curr = curr.right_leaf
            else:
                if curr.left_leaf is None:
                    curr.left_leaf = new_node
                    curr.left_leaf.depth = curr.depth + 1
                    if curr.left_leaf.depth > self.left_depth:
                        self.left_depth += 1
                    break
                curr = curr.left_leaf
        self._size += 1

    def search(self, val):
        """Search through the Tree for the Node containing the given value."""
        try:
            if val == self._root.val:
                return self._root
            curr = self._root
            while curr:
                if val > curr.val:
                    if val == curr.right_leaf.val:
                        return curr.right_leaf
                    curr = curr.right_leaf
                else:
                    if val == curr.left_leaf.val:
                        return curr.left_leaf
                    curr = curr.left_leaf
        except AttributeError:
            return None

    def size(self):
        """Return the size of the Tree."""
        return self._size

    def balance(self):
        """Return positive or negative integer depending on the balance."""
        return self.left_depth - self.right_depth

    def depth(self):
        """Return the depth level of the Tree."""
        if self.right_depth > self.left_depth:
            return self.right_depth
        return self.left_depth

    def contains(self, val):
        """Return True if the given value is in the Tree, otherwise return False."""
        try:
            if val == self._root.val:
                return True
            curr = self._root
            while curr:
                if val > curr.val:
                    if val == curr.right_leaf.val:
                        return True
                    curr = curr.right_leaf
                else:
                    if val == curr.left_leaf.val:
                        return True
                    curr = curr.left_leaf
        except AttributeError:
            return False
