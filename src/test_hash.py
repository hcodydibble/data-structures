"""Test functions for the hash module."""
import pytest


def test_empty_dict_on_add_hash_init(add_hash):
    """Test that the Hash table inits with empty dict."""
    assert add_hash._table == {}


def test_max_size_default_on_add_hash(add_hash):
    """Test that the Hash tables max size defaults to 20."""
    assert add_hash._max == 20


def test_set_adds_something_on_add_hash(add_hash):
    """Test that something gets added when using the set method."""
    add_hash.set('apple', 'apple')
    assert len(add_hash._table) == 1


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
    from hash import Hash
    h = Hash(style='break')
    with pytest.raises(ValueError):
        h.set('apple', 'apple')
