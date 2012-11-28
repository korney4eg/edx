import random
def takeBall(bucket):
    """returns a random int between 1 and 6"""
    return random.choice(bucket)
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here

    yes = 0
    for i in range(numTrials):
        bucket = ['R','R','R','G','G','G']
        r = []
        
        for j in range(3):
            r.append(takeBall(bucket)) 
            bucket.remove(r[-1])
        if str(r[0])+str(r[1])+str(r[2]) =='GGG' or str(r[0])+str(r[1])+str(r[2]) =='RRR':
            yes += 1
    return yes*1.0/numTrials

print noReplacementSimulation(5000)