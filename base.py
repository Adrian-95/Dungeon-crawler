import random

class Dice(int):
    def __new__(self, sides=100):
        self.sides=sides
        self.value=self.getValue(self)
        self.values=[]
        return super(self, self).__new__(self, self.value)

    def getValue(self):
        return random.randrange(self.sides)+1
        return x

    def __repr__(self):
        return str(self.value)

    def __mul__(self, other):
        self.values=[]
        for die in range(other):
            self.values.append(self.getValue() )
        self.value = sum(self.values)
        return self

    __rmul__ = __mul__

    def highest(self, num):
        self.values.sort()
        print(self.values)
        self.value = sum(self.values[-num:])
        return self
    
    def lowest(self, num):
        self.values.sort()
        print(self.values)
        self.value = sum(self.values[:num])
        return self

class Dungeon(object):
    def __init__(self):
        pass

class City(object):
    def __init__(self):
        pass

class Room(object):
    def __init__(self):
        pass

