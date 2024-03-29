# # Bubble Sort
# In the worst case scenario (when the list is in reverse order),
# this algorithm would have to swap every single item of the array.
# Our swapped flag would be set to True on every iteration.
# Therefore, if we have n elements in our list,
# we would have n iterations per item
# thus Bubble Sort's time complexity is O(n^2).

def bubble_sort(input_list: list) -> list:
    # We set swapped to True so the loop looks runs at least once
    length = len(input_list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(length - 1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                swapped = True
    return input_list


print(bubble_sort([2, 4, 75, 41, 45, 34, 3]))
print(bubble_sort([]))
print(bubble_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(bubble_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(bubble_sort([1, 2, 5, 41, 3, 45, 34, 3]))
