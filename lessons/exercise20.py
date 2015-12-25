from sys import argv

script, file = argv


#print full file content
def printFullFile(current_file):
    print("We will print the full file.")
    print (current_file.read())


# print file content line by line
def printLineFile(current_file):
    print("> %s" %(current_file.readline()))


# get back to file beginning
def rewine (current_file):
    current_file.seek(0)

#open the file
current_file = open(file)

printFullFile(current_file=current_file)
print("Let's rewine to the back")
rewine(current_file=current_file)
print("Let's print line by line three times.")
printLineFile(current_file)
printLineFile(current_file)
printLineFile(current_file)