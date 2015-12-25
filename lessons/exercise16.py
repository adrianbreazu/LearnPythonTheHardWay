from sys import argv

script, file_name = argv

print ("We're going to erase file %s" %file_name)
print ("If you donn't want that, hit CTRL+C (^C).")
print ("If you do want that, hit RETURN. ")
input('?')

print ("Open the file ...")
txt = open(file_name, 'w')

print ("Truncate the file ...")
txt.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input ("> ")
line2 = input ("> ")
line3 = input ('> ')

print ("I'm going to write these to the file.")

txt.write(line1 + '\n')
txt.write(line2 + '\n')
txt.writelines(line3 + '\n')
txt.writelines("another writelines command")

print ("and finally, we close the file")
txt.close()