"""Test functions for the various sorting functions.
    
    It will be starting with bubble sort, each following 
    sort function will have its own preceeding doc string.
"""
import pytest


BUBBLE_SORT_TESTS = [
    ([28, 23, 32, 4, 6, 33, 13, 34, 17, 24], [4, 6, 13, 17, 23, 28, 32, 33, 24, 34]),
    ([14, 18, 3, 6, 5, 23, 37, 30, 36, 28, 28, 24, 13, 15, 1], [3, 5, 6, 13, 14, 15, 18, 23, 24, 28, 28, 30, 36, 1, 37]),
    ([-32, -14, 0, -10, -12, -31, -18, -11, -21, -6], [-32, -31, -21, -18, -14, -12, -11, -10, -6, 0]),
    ([20, 37, 36, 40, 2, 2, 21, 36, 28, 27, 5, 26, 34, 10, 31], [2, 2, 5, 10, 20, 21, 26, 27, 28, 34, 36, 36, 37, 31, 40]),
    ([6.12, 22.82, 14.23, 10.01, 4.84, 37.1, 34.72, 37.05, 26.78, 10.32, 4.18, 16.18, 19.018, 1.53, 1.72], [1.53, 4.18, 4.84, 6.12, 10.01, 10.32, 14.23, 16.18, 19.018, 22.82, 26.78, 34.72, 37.05, 1.72, 37.1]),
    ([39, 458, 100, 379, 1, 167, 75, 208, 3, 275, 100, 234, 36, 198, 39, 173, 34, 259, 90, 105], [1, 3, 34, 36, 39, 39, 75, 90, 100, 100, 167, 173, 198, 208, 234, 259, 275, 379, 105, 458]),
]


@pytest.mark.parametrize("the_list, result", BUBBLE_SORT_TESTS)
def test_bubble_sort_on_various_lists(the_list, result):
    """Test that, given various lists, the bubble sort function will return the expected result."""
    from bubble_sort import bubble_sort
    assert bubble_sort(the_list) == result