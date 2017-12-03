"""Test functions for the trie module."""
import pytest


def test_trie_inserts_string(empty_trie):
    """Test that the head Nodes child is the first letter of the inserted word."""
    empty_trie.insert('test')
    assert empty_trie.head.children['t']


def test_insert_raises_error(empty_trie):
    """Test that insert raises ValueError if anything other than a string is inserted."""
    with pytest.raises(ValueError):
        empty_trie.insert(1)


def test_contains_returns_true(empty_trie):
    """Test that contains returns True if the word is in the trie tree."""
    empty_trie.insert('test')
    assert empty_trie.contains('test')


def test_contains_returns_false(empty_trie):
    """Test that contains returns False if the word isn't in the trie tree."""
    empty_trie.insert('test')
    assert empty_trie.contains('tests') is False


def test_size_returns_correct_string_on_one_word(empty_trie):
    """Test that the size method returns the correct string if only one word in trie tree."""
    empty_trie.insert('test')
    assert empty_trie.size() == "There is one word in the trie tree."


def test_size_returns_correct_string_on_multiple_words(empty_trie):
    """Test that the size method returns the correct string if multiple words in trie tree."""
    empty_trie.insert('test')
    empty_trie.insert('testing')
    empty_trie.insert('tested')
    assert empty_trie.size() == "There are 3 words in the trie tree."


def test_remove_works_on_one_word(empty_trie):
    """Test that remove works when there is one word in the trie tree."""
    empty_trie.insert('test')
    assert empty_trie.contains('test')
    empty_trie.remove('test')
    assert empty_trie.contains('test') is False


def test_remove_removes_only_the_word_to_be_removed(empty_trie):
    """Test that remove only removes the word put in even if it shares letters with another word."""
    empty_trie.insert('tested')
    empty_trie.insert('testing')
    assert empty_trie.contains('testing')


def test_raises_error_if_word_not_in_trie(empty_trie):
    with pytest.raises(ValueError):
        empty_trie.remove('test')
