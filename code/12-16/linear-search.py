from typing import List, Any


def linear_search(input: List, target: Any) -> Any:
    """Linear Search with Time: O(n) and Space O(1)F"""

    if not input:
        return None
    for index in range(len(input)):
        if input[index] == target:
            return index + 1

    return None


if __name__ == "__main__":
    input_integers = [1, 2, 3, 4]
    input_integer_repeats = [2, 3, 4, 5, 1, 2]
    input_strings = ["who", "what", "where"]
    input_floats = [0.222, 0.44444444444444444444444444444, 0.9]

    print(
        f"target 2 on list {input_integers} is at {linear_search(input_integers, 2)}")
    print(
        f"target 2 on list {input_integer_repeats} is at {linear_search(input_integer_repeats, 2)}")
    print(
        f"target 'where' on list {input_strings} is at {linear_search(input_strings, 'where')}")
    print(
        f"target 2 on list {input_strings} is at {linear_search(input_strings, 2)}")
    print(
        f"target 0.9 on list {input_floats} is at {linear_search(input_floats, 0.9)}")
    print(
        f"target (2, 3) on list {input_integers} is at {linear_search(input_integers, (2,3))}")
