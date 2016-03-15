from random import *
from cthulhu import *


class Generation:
    def __init__(self):
    	self.tabIndividus = self.initGeneration()

    def initGeneration(self):
        tab = []
        for y in range(0,10):
            tab.append(Cthulhu())
        return tab

    def printGen(self):
    	tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            persos = perso.getGenes()
            tab2.append(persos)
        print tab2
        return tab2