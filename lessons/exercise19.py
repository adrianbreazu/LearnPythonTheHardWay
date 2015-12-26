def cheese_and_crackers(*args):
    cheese, crackers = args
    print ("You have %s cheese!" % cheese)
    print ("You have %s boxes of crackers!" %crackers)
    print ("Man that's enough for a party!")

print ("""
We can give the function numbers directly on the call.
""")
cheese_and_crackers(20,30)


print ("""
OR, we can use variables from our script:
""")
amount_cheese = 20
amount_crackers = 30
cheese_and_crackers(amount_cheese, amount_crackers)


print ("""
we can also do math when calling the function
""")
cheese_and_crackers(10+10, 10+10+10)


print("""
we can also use math with numbers and variables when calling the function.
""")
cheese_and_crackers(amount_cheese+5, amount_crackers+10)
