"""Test functions for the Binary Search Tree."""


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


def test_contains_returns_true_on_root(rooted_bst):
    """Test that the contain method returns True if the value looked for is the root."""
    assert rooted_bst.contains(10) is True


def test_depth_returns_correct_depths(rooted_bst):
    """Test that depth returns the correct number.

        Sacrificing dots for efficiency.
    """
    rooted_bst.insert(11)
    assert rooted_bst.depth() == 1
    rooted_bst.insert(9)
    assert rooted_bst.depth() == 1
    rooted_bst.insert(12)
    assert rooted_bst.depth() == 2


def test_search_returns_from_right_side(rooted_bst):
    """Test that search will return from the right side of the Tree."""
    rooted_bst.insert(12)
    rooted_bst.insert(11)
    rooted_bst.insert(13)
    rooted_bst.insert(15)
    assert rooted_bst.search(13)


def test_in_order_traversal_yields_something(traversal_bst):
    """Test that the in-order traversal returns something."""
    assert traversal_bst.in_order()


def test_in_order_traversal_returns_value(traversal_bst):
    """Test that the in-order traversal returns the first value."""
    value = traversal_bst.in_order()
    assert next(value) == 0


def test_in_order_traversal_returns_correct_order(traversal_bst):
    """Test that the in-order traversal return values in the correct order."""
    assert [i for i in traversal_bst.in_order()] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_pre_order_traversal_returns_correct_order(traversal_bst):
    """Test that the pre-order traversal returns values in the correct order."""
    assert [i for i in traversal_bst.pre_order()] == [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]


def test_post_order_traversal_returns_correct_order(traversal_bst):
    """Test that the pre-order traversal returns values in the correct order."""
    assert [i for i in traversal_bst.post_order()] == [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7]


def test_breadth_first_traversal_returns_correct_order(traversal_bst):
    """Test that the pre-order traversal returns values in the correct order."""
    assert [i for i in traversal_bst.breadth_first()] == [7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6]


def test_delete_helper_yields_something(traversal_bst):
    """Test that _delete_helper does the same things as breadth_first."""
    assert traversal_bst._delete_helper()


def test_delete_removes_node(traversal_bst):
    """Test that delete removes the Node containing the given value."""
    traversal_bst.delete(5)
    assert [i for i in traversal_bst.in_order()] == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
