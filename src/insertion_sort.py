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


if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint
    best_case = [1, 2, 3, 4, 5, 6, 7]
    worst_case = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    big_numbers = [randint(101, 250) for _ in range(6)]

    best_case = timeit.timeit("insertion_sort(best_case)", setup="from __main__ import best_case, insertion_sort")
    worst_case = timeit.timeit("insertion_sort(worst_case)", setup="from __main__ import worst_case, insertion_sort")
    big_numbers = timeit.timeit("insertion_sort(big_numbers)", setup="from __main__ import big_numbers, insertion_sort")
    print('Best case time: ', best_case)
    print('Worst case time: ', worst_case)
    print('Big numbers list time:', big_numbers)
    