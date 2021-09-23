"""
    Q1: Given a string, you have to insert 'a' into it, subject to the condition
    that the string cannot contain 3 consecutive a's. Return the maximum number
    of a's that can be inserted. For eg: dog: return 8, as you can make aadaaoaagaa.
Q2. Given 3 integers A, B, C, they represent the count of the letters 'a', 'b',
and 'c'. Return any string that contains A as, B bs, and C cs, subject to the
condition that it cannot contain 3 consecutive as, bs, or cs.
For example A=1,B=2,C=3; you may return abccbc.
    """


def checkCharacter(input, test_char):
    result = ""
    for char in input:
        if char != test_char:
            result += "aa"+char

    result += "aa"
    print(result)
    return len(result)


ans = checkCharacter("dog", "a")
print(f"answer is : {ans}")
