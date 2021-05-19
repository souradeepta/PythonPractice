"""Question:
    given an string representation of a binary number.
    It can have 2 operations on it:
    1. "?" : lists the number of 1s in the binary number
        and adds to the output list
    2. "+" : does a binary addition on the number
    Apply the requests and output the result of the operations
    @number = "1101"
    @requests = ["?" ,"+", "?", "+", "+", "?" ]
    @output = [3,3,2]
    1101 ? : ouput[3]
    1101 + : 1110, output[3]
    1110 ? : ouput[3,3]
    1111 + : 10000
    10000 + : 10001
    10001 ? : output[3,3,2]
    """

from typing import List


def binary_manipulation(number: str, requests: List[str]) -> List[int]:
    ans = []
    if not number or not requests:
        return ans

    for request in requests:
        if request == "?":
            ans.append(countChar(number))
        elif request == "+":
            number = binary_string_add(number)
        print(f'Result of {request} is {ans}, {number}')
    return ans


def string_to_binary(input: str) -> int:
    binary_converted = ' '.join(format(c, 'b')
                                for c in bytearray(input, "utf-8"))
    return binary_converted


def binary_string_add(input: str, carry=1) -> str:
    result = ""
    if not input:
        return result

    input = list(input)
    left = 0
    right = len(input) - 1
    while right >= left:
        if input[right] == "0" and carry == 1:
            input[right] = "1"
            carry = 0
        if input[right] == "1" and carry == 1:
            input[right] = "0"
            carry = 1
        if input[right] == "0" and carry == 0:
            input[right] = "0"
        if input[right] == "1" and carry == 0:
            input[right] = "1"

        right -= 1

    if carry == 1:
        result = "".join(input)
        result = "1"+result
    else:
        result = "".join(input)
    # print(input, result)
    return result


def countChar(input: str, char: chr = "1") -> int:
    from collections import Counter
    count = Counter(input)
    return count[char]


def setBits(input: str) -> int:
    byte_list = []
    byte_array = bytearray(input, "ascii")
    for byte in byte_array:
        byte_list.append(bin(byte))
    return byte_list


number = "1101"
requests = ["?", "+", "?", "+", "+", "?"]
output = [3, 3, 1]
assert output == binary_manipulation(number, requests), "output is incorrect"

number = "10001"
requests = ["?", "+", "?", "+", "+", "?"]
output = [2, 2, 2]
assert output == binary_manipulation(number, requests), "output is incorrect"
