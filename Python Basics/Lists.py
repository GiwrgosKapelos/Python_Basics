guests = ["George", "Nick", "Alex", "Helen"] 
emptylist = []

for steps in range(4):
    print(guests[steps])
    
#update a value
guests[3] = "Gwgw"
print(guests[3])

#add a new value to the end of the list
guests.append("Helen")

#display the last value in the list
print(guests[-1])

#delete the first item in the list and print it
del guests[0]
print(guests[0])

guests.remove("Gwgw")
for steps in range(3):
    print(guests[steps])

#Search the list (For more than one same items, it finds the first one)
#print(guests.index("George")) Prints error cause its not in the list

print(guests.index("Alex"))

#find how many entries are in the list
numEntries = len(guests)

for steps in range(numEntries):
    print(guests[steps])
    
#specify the name of your list and a variable name to hold each entry as you go through the loop
for guest in guests:
    print(guest)
    #the variable guests will contain the values as we go through the loop

#Sort the list in alphabetical order
guests.sort()

for guest in guests:
    print(guest)
