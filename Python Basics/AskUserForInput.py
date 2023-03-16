#salary = input("please enter your salary")
#bonus = input("please enter your bonus")

#paycheck = float(salary) + float(bonus)

#print (paycheck)

# Exercise 1
loan = input("What's the cost of the loan? \n")
intrate = input("What's the interest rate? \n")
numyears = input("What's the number of years for the loan? \n")

intrate = float(intrate)/100
print(intrate)

M = (float(loan)*(float(intrate)*(1+float(intrate))*int(numyears))) / ((1+float(intrate))*int(numyears)-1)

print("The output is %.2f" %M)