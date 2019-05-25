# Pure Recursion

def f(num):
    if num == 1:
        result = 0
    else:
        result = 1 + f(num-1)
        if num%3 == 0:
            result = min(result,1+f(num/3))
        if num%2 == 0:
            result = min(result,1+f(num/2))
    return result






# Dynamic Programming

def memo(num):
    if num<1:
        print('you must enter an integer that is at least 1')
    memo = [None] * (num+1)
    memo[1] = 0
    return f(num,memo)


def f(num,memo):
    if memo[num] != None:
        return memo[num]
    else:
        result = 1 + f(num-1,memo)
        if num%3 == 0:
            result = min(result,1+f(num/3,memo))
        if num%2 == 0:
            result = min(result,1+f(num/2,memo))
        memo[num] = result
    return memo[num]






# Bottom Up

def min_step(n):
    memo = [None] * (n+1)
    memo[1],memo[2],memo[3] = 0,1,1
    for i in range(4,n+1):
        result = 1 + memo[i-1]
        if i%2 == 0:
            result = 1 + min(result,memo[i/2])
        if i%3 == 0:
            result = 1 + min(result,memo[i/3])
        memo[i] = result
    return memo[i]


