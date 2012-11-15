def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    minp = 0
    maxp = x
    midp = 0
    privans = 0
    while abs(b**midp - x ) > 0.5:
        midp = (minp+maxp)/2
        if b**midp - x < 0:
            minp = midp
        else:
            maxp = midp
        if midp == privans:
            return midp
        #print('low = ' + str(minp) + ' high = ' + str(maxp) + ' ans = ' + str(b**midp))
        privans = midp
    return midp
