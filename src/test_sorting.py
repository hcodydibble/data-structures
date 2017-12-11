"""Test functions for the various sorting functions.
    
    It will be starting with bubble sort, each following 
    sort function will have its own preceeding doc string.
"""
import pytest


ONE_TEST_TO_RULE_THEM_ALL = [
    ([28, 23, 32, 4, 6, 33, 13, 34, 17, 24], [4, 6, 13, 17, 23, 24, 28, 32, 33, 34]),
    ([14, 18, 3, 6, 5, 23, 37, 30, 36, 28, 28, 24, 13, 15, 1], [1, 3, 5, 6, 13, 14, 15, 18, 23, 24, 28, 28, 30, 36, 37]),
    ([-32, -14, 0, -10, -12, -31, -18, -11, -21, -6], [-32, -31, -21, -18, -14, -12, -11, -10, -6, 0]),
    ([20, 37, 36, 40, 2, 2, 21, 36, 28, 27, 5, 26, 34, 10, 31], [2, 2, 5, 10, 20, 21, 26, 27, 28, 31, 34, 36, 36, 37, 40]),
    ([6.12, 22.82, 14.23, 10.01, 4.84, 37.1, 34.72, 37.05, 26.78, 10.32, 4.18, 16.18, 19.018, 1.53, 1.72], [1.53, 1.72, 4.18, 4.84, 6.12, 10.01, 10.32, 14.23, 16.18, 19.018, 22.82, 26.78, 34.72, 37.05, 37.1]),
    ([39, 458, 100, 379, 1, 167, 75, 208, 3, 275, 100, 234, 36, 198, 39, 173, 34, 259, 90, 105], [1, 3, 34, 36, 39, 39, 75, 90, 100, 100, 105, 167, 173, 198, 208, 234, 259, 275, 379, 458]),
    ([328, 542, 441, 690, 980, 849, 664, 780, 735], [328, 441, 542, 664, 690, 735, 780, 849, 980]),
    ([260, 498, 841, 669, 926, 326, 930, 62, 558, 412], [62, 260, 326, 412, 498, 558, 669, 841, 926, 930]),
    ([797, 265, 456, 381, 462, 305, 14, 921, 528, 636], [14, 265, 305, 381, 456, 462, 528, 636, 797, 921]),
    ([438, 366, 716, 325, 521, 266, 670, 528, 895], [266, 325, 366, 438, 521, 528, 670, 716, 895]),
    ([883, 1, 111, 313, 855, 623, 295, 882, 515, 344], [1, 111, 295, 313, 344, 515, 623, 855, 882, 883]),
    ([369, 926, 440, 948, 876, 88, 591, 670, 54], [54, 88, 369, 440, 591, 670, 876, 926, 948])
]


@pytest.mark.parametrize("the_list, result", ONE_TEST_TO_RULE_THEM_ALL)
def test_bubble_sort_on_various_lists(the_list, result):
    """Test that, given various lists, the bubble sort function will return the expected result."""
    from bubble_sort import bubble_sort
    assert bubble_sort(the_list) == result


"""The following are test functions for the insertion sort function."""


@pytest.mark.parametrize("the_list, result", ONE_TEST_TO_RULE_THEM_ALL)
def test_insertion_sort_on_various_lists(the_list, result):
    """Test that, given various lists, insertion sort will return the expected outcome."""
    from insertion_sort import insertion_sort
    assert insertion_sort(the_list) == result


def test_insertion_sort_raises_error():
    """Test that the insertion sort function will raise an error if given anything but a list."""
    from insertion_sort import insertion_sort
    with pytest.raises(ValueError):
        insertion_sort('WATCH ME BREAK IT LUL')

"""The following are test functions for the merge sort algorithm."""


@pytest.mark.parametrize('the_list, result', ONE_TEST_TO_RULE_THEM_ALL)
def test_merge_sort_on_various_lists(the_list, result):
    """Same as the others honestly."""
    from merge_sort import merge_sort
    assert merge_sort(the_list) == result


def test_merge_sort_raises_error():
    """Test that merge sort will raise an error."""
    from merge_sort import merge_sort
    with pytest.raises(ValueError):
        merge_sort('BROKE AF')

"""The following are test funtions for the quick sort algorithm.

    They will look almost exactly like ever other test.
"""


@pytest.mark.parametrize('the_list, result', ONE_TEST_TO_RULE_THEM_ALL)
def test_quick_sort_on_various_lists(the_list, result):
    """Same as the others honestly."""
    from quick_sort import quick_sort
    assert quick_sort(the_list) == result


def test_quick_sort_raises_error():
    """Test that merge sort will raise an error."""
    from quick_sort import quick_sort
    with pytest.raises(ValueError):
        quick_sort('BROKE AF')
