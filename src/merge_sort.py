"""Function for implementing a merge sort algorithm."""


def merge_sort(a_list):
    """Merge sort algorithm."""
    if isinstance(a_list, list):
        if len(a_list) <= 1: 
            return a_list
        left, right = merge_sort(a_list[:len(a_list) // 2]), merge_sort(a_list[len(a_list) // 2:])

        def merge_list(l1, l2):
            output = []
            idx1 = idx2 = 0
            while idx1 < len(l1) and idx2 < len(l2):
                if l1[idx1] < l2[idx2]:
                    output.append(l1[idx1])
                    idx1 += 1
                else:
                    output.append(l2[idx2])
                    idx2 += 1
            if idx1 == len(l1):
                output.extend(l2[idx2:])
            else:
                output.extend(l1[idx1:])
            return output
        return merge_list(left, right)
    else:
        raise ValueError("Lists only")