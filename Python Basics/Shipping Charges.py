import locale

locale.setlocale(locale.LC_ALL, '')
purchase = int(input("Add the amount for your total purchases:"))

if purchase < 50:
    purchase = purchase + 10
    print("Added 10 dollars to your purchases!")
else :
    print("Shipping is free!")
    
finalpurchases = "{:,}".format(purchase)
print("Your total is " + "$", finalpurchases)
print("Your total is "+locale.currency(purchase, grouping=True))