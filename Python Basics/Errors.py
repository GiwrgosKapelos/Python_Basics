# firstNumber = float(input("Enter a number: "))
# secondNumber = float(input("Enter a number: "))

# try:
#     result = firstNumber / secondNumber
#     print(result)
# except:
#     print("I'm sorry, something went wrong")
    
#-----------------------------------------------------------------------------------------
    
#If you want to know what the error was, you can use the function sys.exc_inf() 
# import sys

# firstNumber = float(input("Enter a number: "))
# secondNumber = float(input("Enter a number: "))
# try:
#     result = firstNumber / secondNumber
#     print(result)
# except:
#     error = sys.exc_info()[0]
#     print("I'm sorry, something went wrong")
#     print(error)
# finally:
#     print("I will always run!") # Whatever is inside the finally, will always run

#-----------------------------------------------------------------------------------------

# firstNumber = float(input("Enter a number: "))
# secondNumber = float(input("Enter a number: "))
# try:
#     result = firstNumber / secondNumber
#     print(result)
# except ZeroDivisionError: # We can write the error here and print something if it throws an error 
#     print("The answer is infinity")
# except:
#     error = sys.exc_info()[0]
#     print("I'm sorry, something went wrong")
#     print(error)
# finally:
#     print("I will always run!") # Whatever is inside the finally, will always run


firstNumber = float(input("Enter a number: "))
secondNumber = floa1(input("Enter a number: "))
try:
    result = firstNumber / secondNumber
    print(result)
except \
ZeroDivisionError: # We can write the error here and print something if it throws an error 
    print("The answer is infinity")
    sys.exit() # If the error is thrown, it will print (the answer is infinity) and then will stop
finally:
    print("I will always run!") # Whatever is inside the finally, will always run