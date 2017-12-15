"""Radix sort algorithm function."""


def radix_sort(a_list):
    """Radix sort algorithm."""
    if isinstance(a_list, list):
        num_bucket = {x: [] for x in range(10)}
        output = []
        str_list = [str(x) for x in a_list]
        for x in range(len(str(max(a_list)))):
            for num in str_list:
                try:
                    num_bucket[int(num[-x+-1])].append(int(num))
                except IndexError:
                    num_bucket[0].append(int(num))
            for j in range(len(num_bucket)):
                while num_bucket[j]:
                    output.append(num_bucket[j].pop(0))
            str_list = [str(x) for x in output]
            output = [] 
        output = [int(x) for x in str_list]
        return output
    else:
        raise ValueError("Lists only")

if __name__ == '__main__':  # pragma: no cover
    import timeit
    from random import randint
    short_list = [randint(1, 50) for _ in range(10)]
    long_list = [randint(1, 50) for _ in range(100)]
    small_numbers = [randint(1, 25) for _ in range(15)]
    big_numbers = [randint(101, 250) for _ in range(15)]

    short_list = timeit.timeit("radix_sort(short_list)", setup="from __main__ import short_list, radix_sort")
    long_list = timeit.timeit("radix_sort(long_list)", setup="from __main__ import long_list, radix_sort")
    small_numbers = timeit.timeit("radix_sort(small_numbers)", setup="from __main__ import small_numbers, radix_sort")
    big_numbers = timeit.timeit("radix_sort(big_numbers)", setup="from __main__ import big_numbers, radix_sort")
    print('Short list time: ', short_list)
    print('Long list time: ', long_list)
    print('Small number list time: ', small_numbers)
    print('Big numbers list time:', big_numbers)
