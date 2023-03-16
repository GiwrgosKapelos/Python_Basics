#Read to file
filename = "demo2.txt"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"
READ = "r"

myFile = open(filename, mode = READ)

fileContent = myFile.read() #returns the entire file in a string
print(fileContent)
fileContent = myFile.readlines() #returns each line at a time
print(fileContent)
print("File was readed successfully")

myFile.close()