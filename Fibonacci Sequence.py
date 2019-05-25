

# Method 1
def feb(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = feb(n-1) + feb(n-2)
    return result




# Method 2
def feb2(n):
    memo = [None] * (n+1)
    return feb_memo(n,memo)
    
def feb_memo(n,memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = feb_memo(n-1,memo) + feb_memo(n-2,memo)
    memo[n] = result
    return result



# Method 3
def bottom_up(n):
    if n == 1 or n == 2:
        return 1
    memo = [None] * (n+1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]