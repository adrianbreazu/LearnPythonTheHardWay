from sys import argv

script, file_to_read = argv

txt = open(file_to_read)

print ("Here's your file %s " %file_to_read)
print (txt.read())

print ("Type the file name again:" )
file_to_read = input('> ')

txt = open(file_to_read)
print (txt.read())