def reverse(x: int) -> int:
    INT_MAX = 2**32-1
    INT_MIN = -2**32
    ans = 0
    neg_sign = False
    if x < 0:
        neg_sign = True
    
    x_abs = abs(x)
    
    while  x_abs > 0:
        rem = x_abs % 10
        quo = x_abs //10
        ans = ans*10 + rem
        x_abs = quo
    
    if neg_sign == True:
        ans =  ans*-1
        
    if ans >= INT_MIN and ans <= INT_MAX:
        return ans
    else:
        return  0
        
result = reverse(123)
print(result)
result = reverse(-1235)
print(result)
result = reverse(-12351408304981940241892834)
print(result)