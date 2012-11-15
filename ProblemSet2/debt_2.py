bal = 999999
year_perc = 0.18
month_perc= year_perc /12
month = 1

paid_low = bal/12
paid_hi = (bal*((1+month_perc)**12))/12
paid= (paid_hi + paid_low)/2
epsilon = 0.01

def balanceRest(balance, payment,percent):
    month = 1
    while month <= 12 :
        balance = (balance - payment)*(1+percent)
        month = month +1
    return balance
paidRest=balanceRest(bal,paid,month_perc)
while abs(paidRest)  >  epsilon:
    paidRest=balanceRest(bal,paid,month_perc)
    if paidRest > 0: 
        paid_low = paid
    else:
        paid_hi = paid
    paid = (paid_hi + paid_low)/2    
print "Lowest Payment: ", round(paid,2)     




