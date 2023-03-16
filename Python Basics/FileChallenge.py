filename = "demo.txt"
WRITE = "w"
myFile = open(filename, mode = WRITE)

myFile.write("Doyle McCarty, 27\n")
myFile.write("Jodi Mills, 25\n")
myFile.write("Nicholas Rose, 32\n")
myFile.write("Kian Goddard, 36\n")
myFile.write("Zuha Hanania, 26")
    
print("File written successfully")

myFile.close()