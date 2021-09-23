# mistakes: inner loop range incorrect, swap placement incorrect,
# comparison incorrect
def selection_sort(input: list) -> list:
    for i in range(len(input)):
        min_ele_idx = i
        for j in range(i+1, len(input)):
            if input[j] < input[min_ele_idx]:
                min_ele_idx = j
        input[min_ele_idx], input[i] = input[i], input[min_ele_idx]
    return input


assert(selection_sort([2, 3, 4, 3, 34, 23, 212, 12, 12, 3])
       == [2, 3, 3, 3, 4, 12, 12, 23, 34, 212])
