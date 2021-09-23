# mistakes : range was incorrect in the second loop, placement of swap
# was incorrect. alternate had incorrect implementation of swap
def bubble_sort(input: list) -> list:
    for i in range(len(input)):
        swapped = False
        for j in range(len(input) - 1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
                swapped = True
        if not swapped:
            break
    return input


def bubble_sort_alt(input: list) -> list:
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for j in range(len(input) - 1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]

                has_swapped = True

    return input


assert(bubble_sort_alt([2, 3, 4, 3, 34, 23, 212, 12, 12, 3])
       == [2, 3, 3, 3, 4, 12, 12, 23, 34, 212])
assert(bubble_sort([2, 3, 4, 3, 34, 23, 212, 12, 12, 3])
       == [2, 3, 3, 3, 4, 12, 12, 23, 34, 212])
