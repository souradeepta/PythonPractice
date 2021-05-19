def isPalindrome(s: str) -> bool:
    if s is None:
        return True
    filtered_list = [x.lower() for x in s if x.isalnum()]
    # print(type(filtered_list))
    str_filtered_list = "".join(filtered_list)

    length = len(str_filtered_list)

    for i in range(length//2):
        if str_filtered_list[length - i-1] != str_filtered_list[i]:
            return False

    return True


result = isPalindrome("A man, a plan, a canal: Panama")
print(result)
result2 = isPalindrome("race a car")
print(result2)
