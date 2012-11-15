def isPrime(n):
    if n < 0:
        raise ValueError()
    elif type(n) != int:
        raise TypeError()
    else:
        if n == 1 :
            return True
    d = 2
    while d*d<=n:
        if n%d == 0:
            return False
        d+=1
    return True
