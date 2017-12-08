"""A hash table."""


class HashTable(object):
    """Hash table."""

    def __init__(self, max_size=20, style='additive'):
        """The init values of a hash table."""
        self._max = max_size
        self._table = [[] for _ in range(max_size)]
        self._style = style


    def set(self, key, val):
        """Store given value and the given key."""
        if not all(isinstance(i, str) for i in [key, val]):
            raise ValueError("Only accepting strings. You inserted a {} and a {}".format(type(key).__name__, type(val).__name__))
        hash_key = self._hash(key) % self._max
        key_exists = False
        bucket = self._table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, val))
        else:
            bucket.append((key, val))

    def get(self, key):
        """Return value attached to given key."""
        hash_key = self._hash(key) % self._max
        bucket = self._table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError("Key not in hash table.")

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
