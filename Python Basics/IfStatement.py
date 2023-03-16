# answer=input("Would you like express shipping?")
# if answer =="yes" :# : means then
#     print("That will be an extra 10 dollars.")
#     #All the conditions are the same as the other languages 

# favoriteTeam = input("What is your favorite soccer team?\n")
# if favoriteTeam =="Olympiakos" :
#     print("You are stupid!")
#     print("You are stupid!") #It doesn't need {}
# if not favoriteTeam == "Asteras Tripolis" : # The same as if favoriteTeam != "Asteras Tripolis":
#     print("You are stupid!")
# print("The only soccer team is Asteras Tripolis!")

#ctrl + K + C put multiple lines on #
flag = False
deposit = int(input("How much do you want to deposite?"))
if deposit > 100 :
    print("Enjoy your free toaster!")
    flag = True #Booleans True & False are case sensitive
else :
    print("Enjoy your mug!")
print("Have a nice day!")

if flag :
    print("Congrats!")