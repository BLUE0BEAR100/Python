def total_calc(bill_amount,tip_prec):
#difine function to calculate the tip on bill
    total = bill_amount*(1+0.01*tip_prec)
    total = round(total,2)
    print(f"Please pay ${total}")
#specify only bill amount
#default value of tip percentage is used

total_calc(150,20)