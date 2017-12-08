"""A hash table."""


class Hash(object):
    """Hash table."""

    def __init__(self, max_size=20, style='additive'):
        """The init values of a hash table."""
        self._max = max_size
        self._table = {}
        self._style = style


    def set(self, key, val):
        """Store given value and the given key."""
        if not all(isinstance(i, str) for i in [key, val]):
            raise ValueError("Only accepting strings. You inserted a {} and a {}".format(type(key).__name__, type(val).__name__))
        hashed = self._hash(key)
        index = hashed % self._max
        self._table.setdefault(index, {}).setdefault(hashed, val)

    def get(self, key):
        """Return value attached to given key."""
        hashed = self._hash(key)
        index = hashed % self._max
        table_index = self._table[index]
        return table_index[hashed]

    def _hash(self, key):
        """Hash the given key."""
        if self._style == 'additive':
            ascii_sum = 0
            ascii_vals = [ord(letter) for letter in key]
            for val in ascii_vals:
                ascii_sum += val
            return ascii_sum
        if self._style == 'xor':
            ascii_sum = 0
            ascii_vals = [ord(letter) for letter in key]
            for val in ascii_vals:
                ascii_sum ^= val
            return ascii_sum
        if self._style == 'sax':
            ascii_sum = 0
            ascii_vals = [ord(letter) for letter in key]
            for val in ascii_vals:
                ascii_sum ^= (ascii_sum << 4) ^ (ascii_sum >> 28) ^ val
            return ascii_sum
        raise ValueError('Algorithm not available.')
