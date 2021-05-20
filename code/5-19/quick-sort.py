# Quick Sort
# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.

def partition(nums: list, low: int, high: int) -> int:
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(input_list: list) -> list:
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(input_list, 0, len(input_list) - 1)
    return input_list


print(quick_sort([2, 4, 75, 41, 45, 34, 3]))
print(quick_sort([]))
print(quick_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(quick_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(quick_sort([1, 2, 5, 41, 3, 45, 34, 3]))
