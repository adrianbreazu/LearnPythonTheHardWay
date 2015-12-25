from sys import argv

script, name = argv
prompt = '> '

print ("Hi %s, my name is %s" %(name, script))
print ("I'll like to ask you a few quetions.")

print ("Do you like me %s? " %name)
likes = input(prompt)
print("Where do you live %s? " %name)
lives = input(prompt)
print ("What kind of computer do you have %s ?" %name)
computer = input(prompt)

print ('''
Alright, so you said %s about likeing me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
''' %(likes, lives, computer))