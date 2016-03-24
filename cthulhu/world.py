from cthulhu import *
from generation import *

class World:

    azeret = raw_input('Number of generations ?  ')
    nbGenerations =int(azeret) #doit etre pair

    genInit = Generation()
    print genInit.tabIndividus

    def __init__(self):
        self.initWorld()

    def initWorld(self):
        CC1 = Cthulhu()
        CC2 = Cthulhu()
        for y in range(0,self.nbGenerations):
            print "GENRATION NUM." + str(y)
            i=0
            while i < len(self.genInit.tabIndividus)/2:
                tab = []
                #tab.append(self.genInit.copulation(self.genInit.tabIndividus[0],self.genInit.tabIndividus[1]))
                etape1 = self.genInit.RWS()
                #print "etape1: " + str(etape1)
                #print "etape1" + str(etape1)
                etape2 = self.genInit.copulation(etape1[0],etape1[1])	
                CC1.setGenes(etape1[0])
                CC2.setGenes(etape1[1])
                score1 = CC1.fitness()
                score2 = CC2.fitness()
                score1 = score1.score
                score2 = score2.score
                print str(etape2[0]) + "score: " + str(score1)
                print str(etape2[1]) + "score: " + str(score2)
                i+=1