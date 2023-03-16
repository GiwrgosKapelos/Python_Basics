import datetime

currentTime = datetime.datetime.now()
today = datetime.date.today()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

print(datetime.datetime.strftime(currentTime, "%H:%M"))
# %H 24 HOUR CLOCK  %l 12 HOUR CLOCK %p AM OR PM %m MINUTES %S SECONDS

#The function strftime can also be used to format time the same as for dates but the parameters are specific to time.

#Exercise 2 Deadline

deadline = input("What is your deadline? (mm/dd/yyyy)\n")
deadlinedate = datetime.datetime.strptime(deadline, "%m/%d/%Y").date() 
print(deadlinedate)

finaledeadline = deadlinedate - today
print(finaledeadline)