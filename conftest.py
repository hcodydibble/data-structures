"""Fixtures for data structure tests."""
import pytest

@pytest.fixture
def empty_bst():
    from bst import Tree
    tree = Tree()
    return tree


@pytest.fixture
def rooted_bst():
    from bst import Tree
    tree = Tree()
    tree.insert(10)
    return tree


@pytest.fixture
def traversal_bst():
    from bst import Tree
    tree = Tree([7, 1, 9, 0, 3, 8, 10, 2, 5, 4, 6])
    return tree


@pytest.fixture
def empty_dll():
    from dll import DLL
    dll = DLL()
    return dll


@pytest.fixture
def filled_dll():
    from dll import DLL
    dll = DLL()
    [dll.push(x) for x in range(1, 3)]
    [dll.append(x) for x in range(3, 6)]
    return dll


@pytest.fixture
def empty_deq():
    from deque import Deque
    d = Deque()
    return d


@pytest.fixture
def add_hash():
    from hash import Hash
    h = Hash()
    return h


@pytest.fixture
def xor_hash():
    from hash import Hash
    h = Hash(hash_style='xor')
    return h


@pytest.fixture
def sax_hash():
    from hash import Hash
    h = Hash(hash_style='sax')
    return h
