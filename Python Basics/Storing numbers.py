width = 20
height = 5

area = width * height
perimeter = 2*width + 2*height
perimeter = 2*(width+height)
print(area)

# + Addition 5+2=7
# - Subtraction 5-2=3
# * Multiplication 5*2=10
# / Division 5/2=2.5
# ** Exponent 5**2=25
# % Modulo 5%2=1

# Sometimes you will need to format the number when you display them to users
print('I have %d cats' % 6)
print('I have %3d cats' % 6)
print('I have %03d cats' % 6)
print('I have %f cats' % 6)
print('I have %.2f cats' % 6)

print("The area of the triangle is %.1f" % area)

print("My favorite number is %d" % 23)

# You can also use a format method to format numeric values, using place holders
print('I have {0:d} cats' .format(6))
print('I have {0:3d} cats' .format(6))
print('I have {0:03d} cats' .format(6))
print('I have {0:f} cats' .format(6))
print('I have {0:.2f} cats' .format(6))
#              ^                  ^            ^
#              |                  0 position   1 position
# Print the think in o position, in out case the 6

print("The are of the triangle would be {0:f} " .format(area))
print("My favorite number is {0:d}" .format(23))

print("Here are three number!" +  
    " The first is: {0:d} The second in: {1:f} The third is: {2:.2f}".format(6, 7, 8))
# ^ Dont get rid of this space