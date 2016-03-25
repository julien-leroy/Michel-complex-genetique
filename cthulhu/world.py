from cthulhu import *
from generation import *

class World:

    azeret = raw_input('Number of generations ?  ')
    ioogyu = raw_input('RWS tapez 1, tournament tapez 2 : ')
    nbGenerations =int(azeret) #doit etre pair
    gen = Generation(ioogyu)
    firstMoyenne = gen.getMoyenne()

    def __init__(self):
        self.initWorld()

    def initWorld(self):
        
        def nextGen():
            newgen = self.gen.CreateNewGen()
            newNewgen = Generation(self.ioogyu).setIndividus(newgen)
            return newNewgen

        print "GENRATION NUM. 0"
        self.gen.printGen()
        
        for y in range(1,self.nbGenerations):
            self.gen = nextGen()
            print "GENRATION NUM. " + str(y)
            self.gen.printGen()

        self.gen.printIndicateurs()
        print "Vous avez choisie ", self.ioogyu , "en mode de selection"
        print "Moyenne initiale   : ", self.firstMoyenne
        print "Moyenne final      : ", self.gen.getMoyenne()
