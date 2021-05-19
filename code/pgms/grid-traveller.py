    """Find the total number of paths in rectangular grid

    Returns:
        int: paths
    """

from typing import Dict


def pathsInGrid(rows: int, cols: int, memo: Dict):
    if rows == 0 or cols == 0:
        return 0

    if rows == 1 and cols == 1:
        return 1

    key = str(rows) + "," + str(cols)
    if key in memo:
        return memo[key]

    memo[key] = pathsInGrid(rows - 1, cols, memo) +  \
        pathsInGrid(rows, cols - 1, memo)

    return memo[key]


print(pathsInGrid(3, 3, {}))
print(pathsInGrid(13, 13, {}))
