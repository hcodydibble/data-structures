"""Test functions for the deq_ module."""
import pytest

def test_deque_is_instance_of_deque_object(empty_deq):
    """Test deque is instance of Deque()."""
    from deque import Deque
    assert isinstance(empty_deq, Deque)


def test_deque_is_instance_of_dll(empty_deq):
    """Test deque inherits from DoublyLinkedList."""
    from dll import DLL
    assert isinstance(empty_deq._dll, DLL)


def test_append_adds_a_value(empty_deq):
    """Test the append method adds value."""
    empty_deq.append(2)
    assert empty_deq._dll.tail.data == 2


def test_append_adds_multiple_values_and_checks_back(empty_deq):
    """Test the append method adds value."""
    empty_deq.append(2)
    empty_deq.append(3)
    assert empty_deq._dll.tail.data == 3


def test_deque_removes_first_node_added(empty_deq):
    """Test that node dedequed is first node added."""
    empty_deq.append(2)
    remove = empty_deq.popleft()
    assert remove == 2


def test_popleft_removes_first_node_added_even_with_multiple_nodes(empty_deq):
    """Test that node popleft'd is first node added even with multiple nodes."""
    empty_deq.append(2)
    empty_deq.append(3)
    remove = empty_deq.popleft()
    assert remove == 2


def test_popleft_raises_exception_on_empty_deque(empty_deq):
    """Test that index error is raised when dequeuing empty deque."""
    with pytest.raises(IndexError):
        empty_deq.popleft()


def test_peek_returns_next_value_to_be_dedequed(empty_deq):
    """Test that value returned is from node next to be dedequed."""
    empty_deq.append(2)
    assert empty_deq.peek() == 2


def test_peek_returns_none_on_empty_deque(empty_deq):
    """Test that None is returned on empty list peek."""
    assert empty_deq.peek() is None


def test_size_method_returns_list_length_0_if_empty(empty_deq):
    """Test size method returns 0 on empty deque."""
    assert empty_deq._dll._counter == 0


def test_size_method_returns_list_length(empty_deq):
    """Test size method on deque."""
    empty_deq.append(2)
    empty_deq.append(3)
    assert empty_deq._dll._counter == 2


def test_len_function_works_with_deque(empty_deq):
    """Test that deque works with len function."""
    assert empty_deq._dll._counter == 0


def test_deque_append_left_adds_node_to_front_of_deque(empty_deq):
    """Test that append adds node at the front."""
    empty_deq.appendleft(1)
    assert empty_deq._dll.head.data == 1
    assert empty_deq._dll.tail.data == 1


def test_deque_append_left_adds_multiple_nodes_to_front_of_deque(empty_deq):
    """Test that append adds node at the front."""
    empty_deq.appendleft(1)
    empty_deq.appendleft(2)
    empty_deq.appendleft(3)
    empty_deq.appendleft(4)
    assert empty_deq._dll.head.data == 4


def test_deque_pop_removes_node_at_end_of_deque(empty_deq):
    """Test that pop removes the tail node."""
    empty_deq.append(2)
    empty_deq.append(3)
    assert empty_deq.pop() == 3


def test_deque_pop_raises_index_error_on_empty_deque(empty_deq):
    """Test that pop raises IndexError on an empty deque."""
    with pytest.raises(IndexError):
        empty_deq.pop()


def test_deque_peek_left_shows_value_of_node_at_head(empty_deq):
    """Test that peekleft shows next node value that would be removed by popleft."""
    empty_deq.append(2)
    empty_deq.appendleft(5)
    assert empty_deq.peekleft() == 5


def test_deque_peek_left_raises_error_on_empty_list(empty_deq):
    """Test that peekleft returns None on an empty list."""
    assert empty_deq.peekleft() is None


def test_size_returns_deque_size(empty_deq):
    """Test that the size method returns correct size."""
    assert empty_deq.size() == 0
