#Open the file
#myFile = open(filename, accessMode)

#filename = The name of the file WITH the extension
#If not give the exact location of the file, it will be made inside the folder of this project

#accessMode = Specify what you will do with the file after you open it
#r = Read the file (Default mode)
#w = Write toy the file
#a = Append to the existing file
#b = Open a binary file
#If you want to read and write use mode = r+ or mode = w+
#With the w you rewrite the whole file, the a continues the writing inside the file

filename = "demo.txt"
accessMode = "w"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"

myFile = open(filename, mode = WRITE)
#myFile = open(filename, mode = accessMode)
#myFile = open(filename, mode = WRITE)


#Write to file
for steps in range(20):
    myFile.write("Hello there, how are you ?\n")
myFile.write(" how are you ?")

print("File written successfully")



myFile.close()#Always call close