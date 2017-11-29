"""Test functions for the Doubly Linked List."""
import pytest


def test_node_has_attributes():
    """Test that the node has attributes."""
    from dll import Node
    n = Node(1, None)
    assert n.data
    assert n.nxt is None
    assert n.prev is None


def test_double_linked_list_has_head(empty_dll):
    """Test if the linked list has head node."""
    assert empty_dll.head is None


def test_double_linked_list_push_adds_new_item(empty_dll):
    """Test that if new node is added."""
    empty_dll.push('val')
    assert empty_dll.head.data == 'val'


def test_double_linked_list_push_two_last_value_is_head(empty_dll):
    """Test that two nodes are added."""
    empty_dll.push('val')
    empty_dll.push('val2')
    assert empty_dll.head.data == 'val2'


def test_double_linked_list_moves_old_head_to_next(empty_dll):
    """Test that the new node is moved to head."""
    empty_dll.push('val')
    empty_dll.push('val2')
    assert empty_dll.head.nxt.data == 'val'


def test_double_linked_list_pop_removes_head_returns_value(empty_dll):
    """Test pop removes head."""
    empty_dll.push('potato')
    empty_dll.pop()
    assert empty_dll.head is None


def test_double_linked_list_pop_returns_head_value(empty_dll):
    """Test pop returns value."""
    empty_dll.push('potato')
    output = empty_dll.pop()
    assert output == 'potato'


def test_double_linked_list_pop_shifts_head_properly(empty_dll):
    """Test pop shifts head."""
    empty_dll.push('potato')
    empty_dll.push('cabbage')
    empty_dll.pop()
    assert empty_dll.head.data == 'potato'


def test_double_linked_list_pop_empty_raises_exception(empty_dll):
    """Test pop on empty linked list raises exception."""
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_size_method_returns_list_length(empty_dll):
    """Test size method on linked list."""
    assert empty_dll._size() == 0


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length2(empty_dll, n):
    """Test size method on linked list."""
    for i in range(n):
        empty_dll.push(i)
    assert empty_dll._size() == n


def test_double_linked_list_append_value(empty_dll):
    """Test double linked list appends value to tail."""
    for i in range(5):
        empty_dll.push(i)
    empty_dll.append(6)
    tail = empty_dll.tail.data
    assert tail == 6


def test_double_linked_list_shift_method(empty_dll):
    """Test double linked list removes last value."""
    for i in range(5):
        empty_dll.push(i)
    empty_dll.shift()
    tail = empty_dll.tail.data
    assert tail == 1


def test_shift_will_not_break_if_pop_and_shift_are_used_on_same_list(empty_dll):
    """Test that shift won't break if it there is nothing in the list."""
    empty_dll.push(2)
    empty_dll.pop()
    with pytest.raises(IndexError):
        empty_dll.shift()


def test_append_on_empty_list(empty_dll):
    """Test that appending on an empty list will set the head to the tail."""
    empty_dll.append('lul')
    assert empty_dll.head.data == 'lul'


def test_remove_empty_list_raises_error(empty_dll):
    """Test that remove on an empty list raises an IndexError."""
    with pytest.raises(IndexError):
        empty_dll.remove(1)


def test_remove_pops_head(empty_dll):
    """Test that remove will pop head if it matches value given."""
    empty_dll.push(1)
    empty_dll.remove(1)
    assert empty_dll.head is None


def test_remove_shifts_tail(empty_dll):
    """Test that remove will shift out the tail if it matches the value given."""
    empty_dll.append(1)
    empty_dll.push(2)
    empty_dll.remove(1)
    assert empty_dll.tail.data == 2


def test_remove_gets_other_node(filled_dll):
    """Test that remove works as I'm assuming it should."""
    assert len(filled_dll) == 5
    filled_dll.remove(4)
    assert len(filled_dll) == 4


def test_remove_raises_error(empty_dll):
    """Test remove raises ValueError if no Node contains given value."""
    empty_dll.push(2)
    empty_dll.push(5)
    with pytest.raises(ValueError):
        empty_dll.remove(3)
