# Insertion Sort
# In the worst case scenario, an array would be sorted in reverse order.
# The outer for loop in Insertion Sort function always iterates n-1 times.
# In the worst case scenario, the inner for loop would swap once,
# then swap two and so forth.
# The amount of swaps would then be 1 + 2 + ... + (n - 3) + (n - 2) + (n - 1)
# which gives Insertion Sort a time complexity of O(n^2).

def insertion_sort(input_list: list) -> list:
    length = len(input_list)
    # Start on the second element as we assume the first element is sorted
    for i in range(1, length):
        item = input_list[i]
        # And keep a reference of the index of the previous element
        j = i-1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and input_list[j] > item:
            input_list[j+1] = input_list[j]
            j -= 1

        # Insert the item
        input_list[j + 1] = item

    return input_list


print(insertion_sort([2, 4, 75, 41, 45, 34, 3]))
print(insertion_sort([]))
print(insertion_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(insertion_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(insertion_sort([1, 2, 5, 41, 3, 45, 34, 3]))
