"""Question:
    given a string representation of a number.
    Find the count of all substrings divisible by 3,
    provided the substring doesnt start with 0 then it is 0
    note: "0" is divisible by 3 since its not "03"
    "456" has substrings ["4", "5, "6", "45", "56", "456"]
    @input =  "456"
    @output = 3
    python: a=1, a+=True, a=2
    """


def substring_divisibility(input: str) -> int:
    ans = 0
    if not input:
        return ans

    substrs = []
    # for i in range(len(input)):
    # substrs.append(input[i])

    for i in range(len(input)):
        for j in range(i, len(input)):
            substrs.append(input[i:j+1])

    substrs = list(set(substrs))

    #remove "0" starting strs
    for s in substrs:
        if len(s) > 1 and s[0] == "0":
            substrs.remove(s)
    print(substrs)

    for s in substrs:
        ans += divisibility(s)
    # print(ans)
    return ans


def divisibility(num: str, divisor=3) -> bool:
    if int(num) % divisor == 0:
        return True
    else:
        return False


input = "456"
output = 3

assert output == substring_divisibility(input), "output is incorrect"

input = "303"
output = 4

assert output == substring_divisibility(input), "output is incorrect"
