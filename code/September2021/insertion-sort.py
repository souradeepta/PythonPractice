# logic forgotten. Different from selection sort. Paritiion based sorting
def insertion_sort(input: list) -> list:
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and key <= input[j]:
            input[j+1] = input[j]
            j -= 1

        input[j+1] = key
    return input


assert(insertion_sort([2, 3, 4, 3, 34, 23, 212, 12, 12, 3])
       == [2, 3, 3, 3, 4, 12, 12, 23, 34, 212])
