import random


class Computer:
    guess = 0
    err = 0
    def __init__(self, _down, _up):
        self.down = _down
        self.up = _up
        self.counter = 0

    def guessnumber(self):
        if self.control()==1:
            self.guess = random.randint(self.down, self.up)
            self.counter += 1
            return self.guess
        else:
            self.error()

    def upp(self):
        if self.control()==1:
            self.down = self.guess + 1
        else:
            self.error()

    def downn(self):
        if self.control()==1:
            self.up = self.guess - 1
        else:
            self.error()

    def control(self):
        if self.up > self.down:
            return 1
        else:
            return 0

    def getcount(self):
        return self.counter

    def error(self):
        print "Up never lower than down, I am good at this thing but you logical intelligence seems to be like bad"
        self.err=1
