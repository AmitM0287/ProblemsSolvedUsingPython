"""
      38 27 43 3 9 82 10
   38 27 43 3       9 82 10
 38 27    43 3     9 82     10
38   27  43  3    9   82   10
 27 38   3 43      9 82    10
   3 27 38 43       9 10 82
    3 9 10 27 38 43 82
"""


def merge(left, right):
    """
    This function sort an array.
    :param left: It's accept a left array as a parameter.
    :param right: It's accept a right array as another parameter.
    :return: It's return the resultant array.
    """
    result = []
    current_index, next_index = 0, 0
    while current_index < len(left) and next_index < len(right):
        if left[current_index] <= right[next_index]:
            result.append(left[current_index])
            current_index += 1
        else:
            result.append(right[next_index])
            next_index += 1
    result += left[current_index:]
    result += right[next_index:]
    return result


def mergesort(lst):
    """
    This function split the given array into two parts.
    :param lst: It's accept a list.
    :return: It's return the merge(left, right).
    """
    if len(lst) <= 1:
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)


if __name__ == '__main__':
    arr = [1, 5, 7, 3, 4, 8, 9]
    print(mergesort(arr))
