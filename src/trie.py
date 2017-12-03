"""A trie tree!"""


class Node(object):

    def __init__(self, label=None, data=None):
        self.data = data
        self.children = dict()

    def add_children(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key


class TrieTree(object):
    """A Trie Tree object."""

    def __init__(self):
        self.head = Node()
        self._word_count = 0

    def insert(self, string):
        """Insert given string into the Trie tree."""
        curr = self.head
        word_finished = True
        string = string.lower()

        for i in range(len(string)):
            if string[i] in curr.children:
                curr = curr.children[string[i]]
            else:
                word_finished = False
                self._word_count += 1
                break

        if not word_finished:
            while i < len(string):
                curr.add_children(string[i])
                curr = curr.children[string[i]]
                i += 1
        curr.data = string


    def contains(self, string):
        """Return True or False depending on if the string is in the Trie or not."""
        curr = self.head
        string = string.lower()

        for i in range(len(string)):
            if string[i] in curr.children:
                curr = curr.children[string[i]]
            else:
                return False
        return True

    def size(self):
        """Return the total number of words in the Trie."""
        if self._word_count == 1:
            return "There is one word in the trie tree."
        else:
            return "There are {} words in the trie tree.".format(self._word_count)

    def remove(self, string):
        """Remove the given string from the Trie."""
        if not self.contains(string):
            raise ValueError("No such string in trie tree.")
        self._remove_helper(string)
        self._word_count -= 1
        

    def _remove_helper(self, string):
        """Helper function to keep the word count correct."""
        curr = self.head
        string = string.lower()
        for i in range(len(string)):
            if not curr.children[string[i]].data:
                curr = curr.children[string[i]]
            elif curr.children[string[i]].data and len(curr.children) == 1:
                curr.data = curr.children[string[i]].data[:-1]
                del curr.children[string[i]]
                self._remove_helper(curr.data)
