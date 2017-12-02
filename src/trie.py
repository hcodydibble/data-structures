"""A trie tree!"""

from linked_list import LinkedList


class TrieTree(object):
    """A Trie Tree object."""

    def __init__(self):
        self._linked = LinkedList()
        self._word_count = 0

    def insert(self, string):
        """Insert given string into the Trie tree."""
        if not isinstance(string, str):
            raise ValueError("That is not a string.")
        pass


    def contains(self, string):
        """Return True or False depending on if the string is in the Trie or not."""
        pass

    def size(self):
        """Return the total number of words in the Trie."""
        pass

    def remove(self, string):
        """Remove the given string from the Trie."""
        pass
