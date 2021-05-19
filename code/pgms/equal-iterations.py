"""Count the number of +1 iterations needed to equalize a numbers array, 
    where all but one element can be incremented each iteration
    """

from typing import List
import time


def countIterations(numbers: List) -> int:
    iterations = 0
    while(True):
        # print(f'element at {iterations} are {numbers}')

        if sameElements(numbers) is True:
            return iterations

        maximum = max(numbers)
        max_index = numbers.index(maximum)

        for i in range(len(numbers)):
            if i != max_index:
                numbers[i] += 1

        iterations += 1


def sameElements(input: List) -> bool:
    """Check if all elements are unique
    even xor would be 0
    odd xor would be that element
    dont do this
    """
    return len(set(input)) <= 1

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

from itertools import groupby
def all_equal2(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


if __name__ == '__main__':
    start = time.time()
    ans = sameElements([1, 3, 4, 5, 5, 3, 3, 3])
    print(f'ans is: {ans}')
    ans = sameElements([3, 3, 3, 3, 3])
    print(f'ans is: {ans}')
    result = countIterations([6, 5, 7, 8, 9, 5, 3, 2, 2, 2, 213, 123, 123, 1, 23, 222123, 3, 23, 2, 3, 23, 12, 3, 12, 3, 23, 1, 23, 12, 3, 123, 12, 31, 2, 234, 23, 423, 42, 34, 234, 23, 42, 34, 23, 4, 6, 54 , 6, 74, 56, 4, 45, 64, 56, 456, 34, 52, 42, 34, 23, 4, 23, 4])

    print(f'result is: {result}')
    result = countIterations([6, 6, 6, 6, 9, ])
    print(f'result is: {result}')
    result = countIterations([6, 6, 6, 6, 6, ])
    print(f'result is: {result}')

    end = time.time()
    print(f'time taken is {end-start} s')
