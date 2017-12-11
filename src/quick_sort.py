"""Function for implementing a quick sort algorithm."""


def quick_sort(a_list):
    """Quick sort algorithm."""
    if isinstance(a_list, list):
        if len(a_list) < 2:
            return a_list
        ref_num = [a_list.pop(0)]
        bigger_nums = []
        smaller_nums = []
        for num in a_list:
            if num > ref_num[0]:
                bigger_nums.append(num)
            else:
                smaller_nums.append(num)
        return quick_sort(smaller_nums) + ref_num + quick_sort(bigger_nums)
    else:
        raise ValueError("Lists only")
