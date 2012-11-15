def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for i in range(n/6,-1,-1):
        for j in range(n/9,-1,-1):
            for k in range(n/20,-1,-1):
                if (i*6+j*9+k*20) == n:
                    return True
    return False
