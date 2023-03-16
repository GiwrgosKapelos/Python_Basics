import datetime
today = datetime.date.today()
print(today) #Printing the today date 
print(today.year)
print(today.month)
print(today.day)

print(today.strftime('%d %b, %Y')) # Changing the format of date
# %d Day, %b Month, %Y Year
# %B Full Month Name %y Two Digit Year %a Part Day of the Week %A Full Day of the Week
print(today.strftime('%A %B, %y')) # Changing the format of date
print(today.strftime('The event is happening at: %d/%B/%Y')) # Changing the format of date

birthday = input("What is your birthday? (mm/dd/yyyy)\n")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date() #.date() Cause I only need the date
print(birthdate)

difference = birthdate - today
print(difference)

#In python you use strftime function to format dates, it takes in the parameters; %d for day, %b for month, and %y for year.
#If your program uses input to take in a date you will need to convert it to a date datatype, 
#the strptime function allows you to do this.