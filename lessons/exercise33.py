def add_elements(array):
    exit_loop = False
    while exit_loop == False:
        element = input('> ')
        if element == 'q:':
            exit_loop = True
        else:
            exit_loop = False
            array.append(element)


def print_elements(array):
    i = 0
    for element in array:
        i = i + 1
        print('The element number %d is %s' % (i, element))


array = []
print('Please enter the next array value. If you want to exit enter q:')
add_elements(array)
print_elements(array)