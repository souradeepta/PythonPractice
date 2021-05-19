# Merge Sort

def merge(a: list, b: list) -> list:
    sorted_list = []
    a_low, b_low = 0, 0
    a_high, b_high = len(a), len(b)
    for _ in range(a_high + b_high):
        if a_low < a_high and b_low < b_high:
            if a[a_low] <= b[b_low]:
                sorted_list.append(a[a_low])
                a_low += 1
            else:
                sorted_list.append(b[b_low])
                b_low += 1

        elif a_low == a_high:
            sorted_list.append(b[b_low])
            b_low += 1
        else:
            sorted_list.append(a[a_low])
            a_low += 1


def merge_sort(input: list) -> list:
    if len(input) <= 1:
        return input

    mid = len(input) // 2
    left_list = merge_sort(input[:mid])
    right_list = merge_sort(input[mid:])

    return merge(left_list, right_list)


print(merge_sort([2, 4, 75, 41, 45, 34, 3]))
print(merge_sort([]))
print(merge_sort([2, -4, 75, -41, 3, -45, 34, 3]))
print(merge_sort([2, 4, 75, 41, 3, 2, 34, 3]))
print(merge_sort([1, 2, 5, 41, 3, 45, 34, 3]))
