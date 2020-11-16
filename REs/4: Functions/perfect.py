def is_perfect(n):
    res = 0
    if n <= 0:
        return False
    for i in range(1,n):
        if n%i==0:
            res += i
    if n==res:
        return True
    else:
        return False