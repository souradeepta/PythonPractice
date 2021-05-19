from typing import List


def bubble_sort(input: List) -> List:
    if not input:
        return []
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[j] < input[i]:
                input[i], input[j] = input[j], input[i]
    return input


print(f'{bubble_sort([3,5,12,1,2,1,5,4])}')
