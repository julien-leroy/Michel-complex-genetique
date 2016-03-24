from cthulhu import *
from generation import *

class World:

    azeret = raw_input('Number of generations ?  ')
    nbGenerations =int(azeret) #doit etre pair
    gen = Generation()

    def __init__(self):
        self.initWorld()

    def initWorld(self):
        
        def nextGen():
            newgen = self.gen.CreateNewGen()

            return Generation().setIndividus(newgen)
        
        for y in range(0,self.nbGenerations):
            print "GENRATION NUM." + str(y)
            self.gen.printGen()

            self.gen = nextGen()
