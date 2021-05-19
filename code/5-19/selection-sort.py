# Selection Sort
# For a list with n elements, the outer loop iterates n times.
# The inner loop iterate n-1 when i is equal to 1, and then n-2 as i is equal to 2 and so forth.
# The amount of comparisons are (n - 1) + (n - 2) + ... + 1,
# which gives Selection Sort a time complexity of O(n^2).

def selection_sort(input: list) -> list:
    length = len(input)
    # This value of i corresponds to how many values were sorted
    for i in range(length):
        # We assume that the first item of the unsorted segment is the smallest
        min_idx = i
        # This loop iterates over the unsorted items
        for j in range(i+1, length):
            if input[j] < input[min_idx]:
                min_idx = j
        # Swap values of the lowest unsorted element with the first unsorted element
        input[i], input[min_idx] = input[min_idx], input[i]
    return input


print(selection_sort([2, 4, 75, 41, 45, 34, 3]))
print(selection_sort([]))
print(selection_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(selection_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(selection_sort([1, 2, 5, 41, 3, 45, 34, 3]))
