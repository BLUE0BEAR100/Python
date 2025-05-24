actual_cost = float(input("Please enter the actual product price"))
sale_amount=float(input("Please enter the sales amount"))

if(sale_amount>actual_cost):
    amount=sale_amount - actual_cost
    print("total Profit = {0}".format(amount))
if(sale_amount==actual_cost):
    amount=actual_cost - sale_amount
    print("No profit No loss")
if(sale_amount<actual_cost):
    amount= actual_cost - sale_amount
    print("total loss = {0}".format(amount))
