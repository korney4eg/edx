# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
        print ("x = "+str(x)+" and n = "+str (n))
    return x

