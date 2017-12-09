"""Function to run an insertion sort algorithm on a given list of numbers."""


def insertion_sort(a_list):
    """Insertion sort function."""
    if isinstance(a_list, list):
        for i in range(len(a_list) - 1):
            for j in range(i + 1, 0, -1):
                if a_list[j] < a_list[j - 1]:
                    a_list[j - 1], a_list[j] = a_list[j], a_list[j - 1]
        return a_list
    else:
        raise ValueError("Lists only")
