# Merge Sort
# The merge_sort function splits its given array in 2,
# and recursively sorts the sub-arrays.
# As the input being recursed is half of what was given,
# like binary trees this takes to process grow logarithmically to n.
# The overall time complexity of the Merge Sort algorithm is O(nlog(n)).
# Requires space to create a new list of the same size as the input list.

def merge(a: list, b: list) -> list:
    sorted_list = []
    # We use the list lengths often, so its handy to make variables
    a_low, b_low = 0, 0
    a_high, b_high = len(a), len(b)

    for _ in range(a_high + b_high):
        if a_low < a_high and b_low < b_high:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if a[a_low] <= b[b_low]:
                sorted_list.append(a[a_low])
                a_low += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(b[b_low])
                b_low += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif a_low == a_high:
            sorted_list.append(b[b_low])
            b_low += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        else:
            sorted_list.append(a[a_low])
            a_low += 1

    return sorted_list


def merge_sort(input_list: list) -> list:
    # If the list is a single element, return it
    if len(input_list) <= 1:
        return input_list

    # Use floor division to get midpoint, indices must be integers
    mid = len(input_list) // 2

    # Sort and merge each half
    left_list = merge_sort(input_list[:mid])
    right_list = merge_sort(input_list[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


print(merge_sort([2, 4, 75, 41, 45, 34, 3]))
print(merge_sort([]))
print(merge_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(merge_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(merge_sort([1, 2, 5, 41, 3, 45, 34, 3]))
