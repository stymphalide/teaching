def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_for(n):
    if n == 0:
        return 1
    else:
        res = 1
        for e in range(1, n+1):
            res = res * e
        return res

        