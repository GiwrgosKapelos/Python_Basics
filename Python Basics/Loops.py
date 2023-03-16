import turtle

# for steps in range(1):
#     turtle.right(45)
#     turtle.color("yellow")
#     turtle.forward(200)
#     turtle.right(135)
#     turtle.color("red")
#     turtle.forward(285)
#     turtle.right(135)
#     turtle.color("blue")
#     turtle.forward(200)

# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
    
# In for statement , I can change the steps variable with whatever i want (i, j, ect), I cant change the word range but i can
# change what is inside the range. This is the number of loops. 

# Nested loops
# for steps in range(10):
#     turtle.right(45)
#     for steps in range(3):
#         turtle.forward(30)
#To find the angle of a x sided object, is turtle.right(360/number of sides i want). For a square is 360/4.

# When range(9) is from 0 to 8, when range(1,4) is from 1 to 3. When range(1,10,2) is from 1 to 9 with step 2.

#One cool thing about Python is the way you can tell it exactly what values you want to use in the loop
# for steps in [1,2,3,4,5]:
#     print(steps)
    
# for steps in ["red", "blue", "green", "black"]:
#     turtle.color(steps)
#     turtle.forward(100)
#     turtle.right(90)

# While Loops

answer = 0

while answer !=4:
    answer=int(input("What is 2+2? "))
    
print("Yes! 2 + 2 = 4")

counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter = counter+1 # counter += 1