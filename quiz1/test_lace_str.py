from lace_str import *
l =[('abc','def'),('','asfdasfd'),('asdffasd',''),('',''),('aaaa','bbbbbbbb')]
n = 0
for i in l :
    n += 1
    if laceS(i[0],i[1]) != laceStrings(i[0],i[1]):
        print 'FATAL  ', n, i[0],i[1],laceS(i[0],i[1]),'!=',laceStrings(i[0],i[1])
    elif len (laceStrings(i[0],i[1])) != len(i[0]+i[1]):
        print 'ERROR in length summ:',len(i[0]+i[1]),len(laceStrings(i[0],i[1])),laceStrings(i[0],i[1]) 
    else:
        print 'TEST OK', n, i[0],i[1], laceStrings(i[0],i[1])