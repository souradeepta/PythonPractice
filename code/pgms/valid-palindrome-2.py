def validPalindrome(s: str) -> bool:
    length = len(s)
    skip = False
    left = 0
    right = length - 1
    while left < right:
        if s[left] != s[right] and skip == False:
            if s[left+1] == s[right]:
                skip = True
                left += 1
            elif s[left] == s[right - 1]:
                right -= 1
                skip = True
            else:
                return False
        elif skip == True:
            return False
        left += 1
        right -= 1

    return True


result = validPalindrome("abbca")
print(result)
result = validPalindrome("eeccccbebaeeabebccceea")
print(result)
