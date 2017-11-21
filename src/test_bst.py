"""Test functions for the Binary Search Tree."""
import random


def test_insert_adds_first_new_node_as_root(empty_bst):
    """Test that the first node added to the Tree is made the root."""
    empty_bst.insert(1)
    assert empty_bst._root.val == 1


def test_new_tree_has_no_root(empty_bst):
    """Test that a new Binary Search Tree has no root."""
    assert empty_bst._root is None


def test_left_leaf_sets_correctly(rooted_bst):
    """Test that adding a Node smaller than root goes to the left."""
    rooted_bst.insert(8)
    assert rooted_bst._root.left_leaf.val == 8


def test_right_leaf_sets_correctly(rooted_bst):
    """Test that adding a Node larger than the root goes to the right."""
    rooted_bst.insert(12)
    assert rooted_bst._root.right_leaf.val == 12


def test_search_returns_root(rooted_bst):
    """Test that search method returns root if its value is what got searched for."""
    assert rooted_bst.search(10) == rooted_bst._root


def test_search_returns_none(empty_bst):
    """Test that search method returns None if value not in Tree."""
    for i in range(5):
        empty_bst.insert(i)
    assert empty_bst.search(10) is None


def test_search_returns_left_side_node(rooted_bst):
    """Test that search returns Node of smaller value."""
    rooted_bst.insert(8)
    rooted_bst.insert(6)
    assert rooted_bst.search(6).val == 6


def test_size_returns(empty_bst):
    """Test that size method returns Tree size count."""
    for i in range(5):
        empty_bst.insert(i)
    assert empty_bst.size() == 5


def test_contains_returns_false(empty_bst):
    """Test that contains methods returns False if value not in Tree."""
    for i in range(5):
        empty_bst.insert(i)
    assert empty_bst.contains(20) is False


def test_contains_returns_true_right(empty_bst):
    """Test that contains method returns True if value is in Tree."""
    for i in range(5):
        empty_bst.insert(i)
    assert empty_bst.contains(3) is True


def test_contains_returns_true_left(rooted_bst):
    """Test that contains method returns True if value is in Tree."""
    rooted_bst.insert(12)
    rooted_bst.insert(2)
    rooted_bst.insert(1)
    assert rooted_bst.contains(2) is True


def test_right_balance_returns_negative(rooted_bst):
    """Test that if Tree is right heavy the balance returns a negative integer."""
    rooted_bst.insert(12)
    rooted_bst.insert(11)
    assert rooted_bst.balance() == -1
