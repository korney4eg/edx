bal = 3926
year_perc = 0.2
month = 1
paid = 10;


def one_year(balance, payment,percent):
    month = 1
    while month <= 12 :
        balance = (balance - payment)*(1+percent/12)
        month = month +1
    return balance

while one_year(bal,paid,year_perc) > 0 :
    paid = paid + 10
print ("Lowest Payment: "+ str(paid))


