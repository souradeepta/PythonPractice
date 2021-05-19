from typing import List, Any


def binary_search(input: List, target: Any) -> None:
    """Binary search with Time O(Log(n)) and Space O(1)"""
    
    if not input:
        return None
    left = 0
    right = len(input)

    while left <= right:
        mid = left + (right - left) // 2
        if input[mid] == target:
            return mid + 1
        elif input[mid] < target:
            left = mid
        else:
            right = mid

    return None


if __name__ == "__main__":
    input_integers = [1, 2, 3, 4]
    input_integer_repeats = [1, 2, 2, 4, 9, 12]
    input_strings = ["1who", "2what", "3where"]
    input_floats = [0.222, 0.44444444444444444444444444444, 0.9]

    print(
        f"target 2 on list {input_integers} is at {binary_search(input_integers, 2)}")
    print(
        f"target 2 on list {input_integer_repeats} is at {binary_search(input_integer_repeats, 2)}")
    print(
        f"target '3where' on list {input_strings} is at {binary_search(input_strings, '3where')}")
    print(
        f"target 0.9 on list {input_floats} is at {binary_search(input_floats, 0.9)}")
