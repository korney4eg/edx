def laceS(s1,s2):
    if (len(s1)> 0) and (len(s2)>0):
        return s1[0]+s2[0]+laceStrings(s1[1:], s2[1:])
    else:
        return s1+s2
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    

    """
    i = 0
    res = ''
    done = False
    it = min (len(s1),len(s2))
    for i in range (it):
        res += s1[i] + s2[i]
    if it > 0:
        i +=1
    if len(s1) < len(s2):
        res += s2[i:]
    elif len(s1) > len(s2):
        res += s1[i:]
    return res


    
        
