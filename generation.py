from individu import individu
from randm import randm

class generation:
    def __init__(self):
        self.tabIndividus = self.initGeneration()

    def initGeneration(self):
        tab = []
        for y in range(0,10):
            i = individu()
            tab.append(i.create())
        return tab

    def printGen(self):
        tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            persos = perso.getGenes()
            tab2.append(persos)
        return tab2

    def tournament(self):
        pass