balance = 4842
balance2 = balance
year_perc = 0.2
month_perc = 0.04

payment = 0
paid = 0;



def paym (percent,balance):
    return round(balance*percent,2)


def balan (balancex,payment,rate):
    return round((balancex-payment)*(1+rate/12),2)

def one_year(balance, payment):
    month = 1
    while month <= 12 :
        payment = paym(balance,month_perc)
        balance=(balan(balance,payment,year_perc))
       # balance= balance - payment
       # print ("Month: "+ str(month))
       # print ("Minimum monthly payment: "+ str(payment))
       # print ("Remaining balance: "+ str(balance))
        month = month +1
    return balance
