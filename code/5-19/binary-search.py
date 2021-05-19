# Binary Search
# drawback of binary search is that if there are multiple occurrences
# of an element in the array,
# it does not return the index of the first element,
# but rather the index of the element closest to the middle.
#  it does have some shortcomings, such as its reliance on the // operator
# time complexity of binary search O(log n).

def binary_search(input_list: list, target: int) -> int:
    low = 0
    high = len(input_list)-1
    index = -1
    while (low <= high) and (index == -1):
        mid = (low+high)//2
        if input_list[mid] == target:
            index = mid
        else:
            if target < input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return index


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(binary_search([], 3))
print(binary_search([1, 2, 4, 5, 6, 7, 8], 3))
print(binary_search([1, 2, 3, 4, 15, 16, 17, 18], 18))
