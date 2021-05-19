from typing import List


def compress(chars: List[str]) -> int:
    count = {}
    result = []
    for char in chars:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    for key, value in count.items():
        result.append(key)
        result.append(value)

    return len(result)


result = compress(["a", "a", "b", "b", "c", "c", "c"])
print(result)
