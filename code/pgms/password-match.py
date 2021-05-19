# input1 = 2
# input2 = ["abcd", "cdab"]


# def matches(input1, input2):
#     result = 0
#     for idx in range(input1-1):
#         for inp in input2:
#             i = 0
#             j = 1
#             while(i<len(inp) and j<len(inp)):
#                 if(inp[i]!= inp[j] and (i+j)%2 == 0):


str1 = "abcd"
str2 = "cdab"
i = 0


def runner(list1):
    ans = 0
    if len(list1) == 1:
        return 1
    for i in range(len(list1)-1):
        ans += matchStr(list1[i], list1[i+1])
    return ans


def matchStr(inp1, inp2):
    inp1 = list(inp1)
    inp2 = list(inp2)
    result = 0
    if len(inp1) != len(inp2):
        result = 2
        return result
    i, j = 0, 1
    while i < len(inp1)-1:
        while j < len(inp1)-1:
            if inp1[i] != inp1[j] and (i+j) % 2 == 0:
                inp1[i], inp1[j] = inp1[j], inp1[i]
                if inp1 == inp2:
                    result += 1
                    return result
            j += 1
        i += 1
    result = 2
    return 1


# print(matchStr(str1, str2))
print(runner(["abcd", "abcd", "azaz", "qwer", "abdc"]))
print(runner(["abcd", "cdab", "azaz", "qwer", "abdc"]))
print(runner(["abcd"]))
print(runner(["abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]))
