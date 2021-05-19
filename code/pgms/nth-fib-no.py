import time


def findNthFibonnachiNumberIterative(n: int) -> int:
    """Find the nth fibonacchi number

    Returns:
        int: the number output
    """
    if n <= 2:
        return 1

    first, second = 0, 1

    while n-1:
        third = first + second
        first = second
        second = third
        n -= 1
    return second


def findNthFibonnachiNumberRecurrsive(n: int, memo: dict) -> int:
    if n <= 2:
        return 1

    if(n in memo):
        return memo[n]

    memo[n] = findNthFibonnachiNumberRecurrsive(n - 1, memo) + \
        findNthFibonnachiNumberRecurrsive(n - 2, memo)
    return memo[n]


start = time.time()
result = findNthFibonnachiNumberIterative(7)
end = time.time()
print(f"solved iterative result is {result} in time {end - start}")

start = time.time()
result = findNthFibonnachiNumberRecurrsive(50, {})
end = time.time()
print(f"solved recurrsive result is {result} in time {end - start}")
