"""Test functions for the trie module."""


def test_trie_inserts_string(empty_trie):
    """."""
    empty_trie.insert('test')
    assert empty_trie.head.children['t']