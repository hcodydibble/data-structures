"""Function to run a bubble sort on a given list of numbers."""


def bubble_sort(a_list, loop_count=1):
    """Bubble sort function."""
    for i in range(len(a_list) - loop_count):
        if a_list[i] > a_list[i + 1]:
            tmp = a_list[i + 1]
            a_list[i + 1] = a_list[i]
            a_list[i] = tmp
        else:
            continue
        loop_count += 1
        bubble_sort(a_list, loop_count)
    return a_list

if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint
    short_list = [randint(1, 50) for _ in range(10)]
    long_list = [randint(1, 50) for _ in range(100)]
    small_numbers = [randint(1, 25) for _ in range(15)]
    big_numbers = [randint(101, 250) for _ in range(15)]
    mix_list = [x for x in zip(small_numbers, big_numbers)]

    short_list = timeit.timeit("bubble_sort(short_list)", setup="from __main__ import short_list, bubble_sort")
    long_list = timeit.timeit("bubble_sort(long_list)", setup="from __main__ import long_list, bubble_sort")
    small_numbers = timeit.timeit("bubble_sort(small_numbers)", setup="from __main__ import small_numbers, bubble_sort")
    big_numbers = timeit.timeit("bubble_sort(big_numbers)", setup="from __main__ import big_numbers, bubble_sort")
    mix_list = timeit.timeit("bubble_sort(mix_list)", setup="from __main__ import mix_list, bubble_sort")
    print('Short list time: ', short_list)
    print('Long list time: ', long_list)
    print('Small number list time: ', small_numbers)
    print('Big numbers list time:', big_numbers)
    print('Mix numbers list time: ', mix_list)
