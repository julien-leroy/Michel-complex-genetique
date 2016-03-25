from cthulhu import *
from generation import *

class World:

    azeret = raw_input('Number of generations ?  ')
    nbGenerations =int(azeret) #doit etre pair
    gen = Generation()
    firstMoyenne = gen.getMoyenne()

    def __init__(self):
        self.initWorld()

    def initWorld(self):
        
        def nextGen():
            newgen = self.gen.CreateNewGen()
            newNewgen = Generation().setIndividus(newgen)
            return newNewgen

        print "GENRATION NUM. 0"
        self.gen.printGen()
        
        for y in range(1,self.nbGenerations):
            self.gen = nextGen()
            print "GENRATION NUM. " + str(y)
            self.gen.printGen()

        self.gen.printIndicateurs()
        print "Moyenne initiale   : ", self.firstMoyenne
        print "Moyenne finale     : ", self.gen.getMoyenne()
