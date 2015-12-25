from sys import argv
from os.path import exists

script, file_read, file_write = argv

print ("Copying from %s to %s." %(file_read, file_write))

in_file = open(file_read)
in_data = in_file.read()

print ("This input file %s is %d bytes long" %(file_read, len(in_data)))

print("Does the output file exists? %s" % exists(file_write))
print ("Ready, hit RETURN to continue, CTRL-C to exist.", input())

out_file = open(file_write, 'w')
out_data = out_file.write(in_data)

print ("Alright, all done.")

out_file.close()
in_file.close()