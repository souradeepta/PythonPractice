# mistakes: forgot to import Any
from typing import Any


def linear_search(input: list, target: Any) -> Any:
    for index in range(len(input)):
        if input[index] == target:
            return index


assert (linear_search([2, 4, 1, 23, 12, 34, 6, 2], 23) == 3)
