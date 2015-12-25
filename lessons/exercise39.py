stuff = {'name':'Zed', 'age':39, 'height':6*12+2}
print (stuff['name'])

stuff['City']='San Francisco'
print(stuff)

del stuff['City']
print (stuff)

# create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#create a basic set of states and come cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add more cities
cities['NY']='Ney York'
cities['OR']='Portland'

# print out some cities
print('-'*5, 'Citieis', '-'*5)
print('NY State has: ', cities['NY'])
print('OR state has: ', cities['OR'])

#print out some states
print('-'*5, 'States', '-'*5)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

#do it by using the state then cities dict
print('-'*16)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

#print every state abbreviation
print('-'*16)
for state, abbreviation in states.items():
    print("%s is abbreviated %s" %(state, abbreviation))

#print every city in state
print('-'*16)
for abbreviation, city in cities.items():
    print("%s has the city: %s" %(abbreviation, city))

#now do both at the same time
print('-'*16)
for state, abbreviation in states.items():
    print('%s has abbreviation %s and has city %s' %(state,abbreviation,cities[abbreviation]))

#safely get a abbreviation by state that might not be there
print('-'*16)
state = states.get('Texas')

if not state:
    print('Sorry, no Texas.')

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print('The city for the state \'TX\' is: ', city)

