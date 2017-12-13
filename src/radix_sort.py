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
