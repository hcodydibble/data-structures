"""Test functions for the hash module."""
import pytest


def test_list_on_add_hash_init(add_hash):
    """Test that the Hash table inits with empty list."""
    assert isinstance(add_hash._table, list)


def test_init_size_of_table(add_hash):
    """Test that the hash table inits with 20 empty buckets."""
    assert len(add_hash._table) == 20


def test_max_size_default_on_add_hash(add_hash):
    """Test that the Hash tables max size defaults to 20."""
    assert add_hash._max == 20


def test_set_adds_something_on_add_hash(add_hash):
    """Test that something gets added when using the set method."""
    add_hash.set('apple', 'apple')
    assert add_hash.get('apple') == 'apple'


def test_set_raises_error(add_hash):
    """Test set method raises ValueError when not given a string."""
    with pytest.raises(ValueError):
        add_hash.set('apple', 4)


def test_get_retrives_given_key_on_add_hash(add_hash):
    """Test the get methods just works."""
    add_hash.set('apple', 'apple')
    assert add_hash.get('apple') == 'apple'


def test_xor_style_set(xor_hash):
    """Test that set works with xor style."""
    xor_hash.set('apple', 'apple')
    assert xor_hash.get('apple')


def test_sax_style_set(sax_hash):
    """Test that set works with sax style."""
    sax_hash.set('apple', 'apple')
    assert sax_hash.get('apple')


def test_hash_method_raises_error():
    """Test that _hash methods raises ValueError if given style not available."""
    from hashtable import HashTable
    h = HashTable(style='break')
    with pytest.raises(ValueError):
        h.set('apple', 'apple')


def test_value_at_key_is_updated(add_hash):
    """Test that adding a value at a key already in table updates that key."""
    add_hash.set('apple', 'cat')
    assert add_hash.get('apple') == 'cat'
    add_hash.set('apple', 'no cat')
    assert add_hash.get('apple') == 'no cat'


def test_get_raises_error(add_hash):
    """Test that the get method raises a KeyError."""
    with pytest.raises(KeyError):
        add_hash.get('apple')
