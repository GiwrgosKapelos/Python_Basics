import csv
#The reader function will take an open csv file and return each row from the file into a list
#dataFromFile = csv.reader(myCSVfile)

#If your file is not using a comma to separate the values, you can tell the reader function what character is used as a delimiter
#dataFromFile = csv.reader(myCSVFile, delimiter=",")

#myCSVFile = the name of the file, delimiter = the thing that separates my data

fileName = "demo.txt"
READ = "r"
with open(fileName, mode = READ) as myCSVFile: #If there is an error during processing, the file will always be closed. I dont need to close the file after.
    #Read the file contents
    dataFromFile = csv.reader(myCSVFile) #returns a list from myCSVFile to dataFromFile 