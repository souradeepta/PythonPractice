from typing import List


def canSumRepeat(target: int, input: List, memo: dict) -> bool:
    """Can the sum of input number lead to the target value

    Args:
        target (int): target
        input (List): list of numbers

    Returns:
        bool: True or False
    """
    if not input:
        return None

    if target == 0:
        return True

    if target < 0:
        return False

    if target in memo:
        return memo[target]

    for elem in input:
        remainder = target - elem
        if(canSumRepeat(remainder, input, memo)):
            memo[target] = True
            return True

    memo[target] = False
    return False


def canSumRepeatList(target: int, input: List, output: List, memo) -> List:
    """Can the sum of input number lead to the target value

    Args:
        target (int): target
        input (List): list of numbers
        output (List): list of numbers which sum to target

    Returns:
        List: List of elements
    """
    if not input:
        return None

    if target == 0:
        return output

    if target < 0:
        return None

    if target in memo:
        return memo[target]

    for elem in input:
        remainder = target - elem
        output.append(elem)
        if(canSumRepeatList(remainder, input, output, {})):
            memo[target] = output
            return output

    memo[target] = None
    return None


print(canSumRepeat(7, [2, 3], {}))  # true
print(canSumRepeat(7, [5, 3, 4, 7], {}))  # true
print(canSumRepeat(8, [2, 3, 5], {}))  # false
print(canSumRepeat(300, [7, 14], {}))  # true

print(canSumRepeatList(7, [2, 3], [], {}))  # true
print(canSumRepeatList(7, [5, 3, 4, 7], [], {}))  # true
print(canSumRepeatList(8, [2, 3, 5], [], {}))  # false
print(canSumRepeatList(300, [7, 14], [], {}))  # true
