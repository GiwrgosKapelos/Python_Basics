#Define this function
#When someone calls this function, execute this code
# def printMessage():
#     print("Hello World!")
#     return

# printMessage()

# #You HAVE to write your functions first and then your main code or call them

# def main():
#     printMessage()
#     printNames()
#     displayMessage("Hello", "George")
#     return

# def printMessage():
#     print("Hello World!")
#     return

# def printNames():
#     names = ["John", "Nick", "Alex"]
#     names.sort()
#     for name in names:
#         print(name)
        
# #Your functions should do ONE thing 

# def displayMessage(greeting, name):
#     message = greeting + ", " + name
#     print(message)
#     return

# #Execute the main function
# main()


def main():
    output = getMessage("John")
    printMessage(output)
    #printmessage(getMessage("John"))
    
def getMessage(name):
    message = "Hello, " + name
    return message # It returns a message
    # return "Hello, " + name

def printMessage(message):
    print(message)
    return

main()
    