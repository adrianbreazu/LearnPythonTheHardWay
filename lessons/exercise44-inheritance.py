class Parent (object):
    def implicit (self):
        print ('Parent implicit()')


    def override(self):
        print ('Parent override()')


    def alter(self):
        print ('Parent alter()')


class Child (Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()


    def override(self):
        print ('Child override()')


    def alter(self):
        print('child before parent alter()')
        super(Child, self).alter()
        print('child after parent alter()')


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alter()
son.alter()