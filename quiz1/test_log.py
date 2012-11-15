from log import *
import math
for i in range(15,50):
    for j in range(2,5):
        if (int(math.log(i,j)) != myLog(i,j)):
            print 'FAIL!! log(',i,',',j,')=',int(math.log(i,j)),'and your =',myLog(i,j)
