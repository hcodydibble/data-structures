"""A Binary Search Tree!"""


class Node(object):
    """A node object."""

    def __init__(self, val, parent=None, left_leaf=None, right_leaf=None):
        self.val = val
        self.parent = parent
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
        if self.search(val):
            return "Node already in Tree"
        if self._root is None:
            self._root = Node(val)
            self._size += 1
            return
        new_node = Node(val)
        curr = self._root
        while curr:
            if new_node.val > curr.val:
                if curr.right_leaf is None:
                    new_node.parent = curr
                    curr.right_leaf = new_node
                    new_node.depth = curr.depth + 1
                    break
                curr = curr.right_leaf
            else:
                if curr.left_leaf is None:
                    new_node.parent = curr
                    curr.left_leaf = new_node
                    new_node.depth = curr.depth + 1
                    break
                curr = curr.left_leaf
        if new_node.val > self._root.val:
            if new_node.depth > self.right_depth:
                self.right_depth += 1
        else:
            if new_node.depth > self.left_depth:
                self.left_depth += 1
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

    def in_order(self):
        """Return a generator that will yield the Tree's values using in-order traversal."""
        stack = []
        node = self._root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left_leaf
            else:
                node = stack.pop()
                yield node.val
                node = node.right_leaf

    def pre_order(self):
        """Return a generator that will yield the Tree's values using pre-order traversal."""
        stack = [self._root]
        while stack:
            node = stack.pop()
            yield node.val
            if node.right_leaf: stack.append(node.right_leaf)
            if node.left_leaf: stack.append(node.left_leaf)

    def post_order(self):
        """Return a generator that will yield the Tree's values using post-order traversal."""
        visited = []
        stack = []
        node = self._root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left_leaf
            else:
                node = stack.pop()
                if node.right_leaf and node.right_leaf not in visited:
                    stack.append(node)
                    node = node.right_leaf
                else:
                    visited.append(node)
                    yield node.val
                    node = None

    def breadth_first(self):
        """Return a generator that will yield the Tree's values using breadth-first traversal."""
        stack = [self._root]
        while stack:
            node = stack[0]
            stack = stack[1:]
            yield node.val
            if node.left_leaf:
                stack.append(node.left_leaf)
            if node.right_leaf:
                stack.append(node.right_leaf)


    def delete(self, val):
        """Delete the Node containing the given value."""
        if val == self._root.val:
            self._root = None
        node_to_delete = self.search(val)
        if node_to_delete:
            if node_to_delete.left_leaf and node_to_delete.right_leaf:
                self._two_children_delete(node_to_delete)
                self._size -= 1
            elif node_to_delete.left_leaf or node_to_delete.right_leaf:
                self._one_child_delete(node_to_delete)
                self._size -= 1
            else:
                self._no_child_delete(node_to_delete)
                self._size -= 1

    def _no_child_delete(self, node):
        """Helper method to delete given node with no children."""
        if node.parent.left_leaf == node:
            node.parent.left_leaf = None
        else:
            node.parent.right_leaf = None

    def _one_child_delete(self, node):
        """Helper method to delete given node with one child."""
        child = node.right_leaf = node.left_leaf
        import pdb; pdb.set_trace()
        if node.parent.left_leaf == node:
            child.parent = node.parent
            node.parent.left_leaf = child
        else:
            child.parent = node.parent
            node.parent.right_leaf = child

    def _two_children_delete(self, node):
        left_child, right_child = node.left_leaf, node.right_leaf
        right_child.left_leaf = left_child
        left_child.parent = right_child
        right_child.parent = node.parent
        if node.parent.left_leaf == node:
            node.parent.left_leaf = right_child
        else:
            node.parent.right_leaf = right_child


if __name__ == '__main__':  # pragma: no cover
    import timeit

    l_imba = Tree([6, 5, 4, 3, 2, 1])
    r_imba = Tree([1, 2, 3, 4, 5, 6])
    sample_tree = Tree([20, 12, 10, 1, 11, 16, 30, 42, 28, 27])

    l_imba = timeit.timeit("l_imba.search(5)", setup="from __main__ import l_imba")
    r_imba = timeit.timeit("r_imba.search(5)", setup="from __main__ import r_imba")
    sample_tree = timeit.timeit("sample_tree.search(16)", setup="from __main__ import sample_tree")

    print('Left-Skewed Search Time: ', l_imba)
    print('Right-Skewed Search Time: ', r_imba)
    print('Balanced Search Time: ', sample_tree)
