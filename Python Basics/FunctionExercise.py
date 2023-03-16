def writeFile(filename,text):
    openFile = open(filename, mode= "w")
    openFile.write(text)
    return

def main():
    writeFile(input("Give the name of the file: "), input("Give the text you want to write: "))
    return

main()