def fib_series(N):
    first = 0
    second = 1
    ans = []
    i = 0
    ans.append(first)
    ans.append(second)
    while i < N-2:
        temp = second
        second = first + second
        first = temp
        ans.append( second)
        i+=1
    return ans

def fib_recur(N):
   
    first = 0
    second = 1
    ans = []
    ans.append(fib_recur())
print(fib_series(10))

