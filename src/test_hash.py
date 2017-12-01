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


# def test_xor_style_set_on(add_hash):
#     """Test that set works with xor style."""
#     add_hash.set('apple', 'apple', 'xor')
#     assert add_hash.get('apple', 'xor')


# def test_sax_style_set(add_hash):
#     """Test that set works with sax style."""
#     add_hash.set('apple', 'apple', 'sax')
#     assert add_hash.get('apple', 'sax')


# def test_hash_method_raises_error(add_hash):
#     """Test that _hash methods raises ValueError if given style not available."""
#     with pytest.raises(ValueError):
#         add_hash.set('apple', 'apple', 'break')
