answer = ""
guests = []
answer = input("Give the name of someone who will attend at your party. Give <done> if you are finished.")
while answer!="done":
    guests.append(answer)
    answer = input("Give the name of someone who will attend at your party. Give <done> if you are finished.")
guests.sort()

for guest in guests:
    print(guest)