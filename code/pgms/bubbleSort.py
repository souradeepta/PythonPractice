from typing import List


def bubble_sort(input: List):
    length = len(input)
    if length < 1:
        return None
    for j in range(length-1):
        for i in range(length - 1 - j):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
    return input


def bubble_sort_optimized(input: List):
    length = len(input)
    if length < 1:
        return None

    swapped = False
    for j in range(length - 1):
        for i in range(length - 1 - j):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
                swapped = True
        if swapped == False:
            return input
    return input


def main():
    sample = [7, 4, 5, 1, 0, 9, 1, 4]
    result = bubble_sort_optimized(sample)
    print(f"output is: {result}")


if __name__ == "__main__":
    main()
