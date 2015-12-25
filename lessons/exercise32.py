hair = ['brown', 'blond', 'red']
eyes = ['blue', 'brown', 'green']
weights = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
money = [1, 'pennies', 2, 'dimes', 3, 'quarters']
my_list = []

for i in range(5):
    print('This is count %d ' % i)

for fruit in fruits:
    print('A fruit of type: %s' % fruit)

for i in range(0,10):
    value = input('> ')
    my_list.append(int(value))

for i in my_list:
    print('Element added was: %d' % i)

