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

    def RWS(self):
        allTabs = self.printGen()
        
        num = self.getAllFitness()
        index1 = randint(0, num)
        index2 = randint(0, num)

        theChosenOne = 0
        theSecondChosenOne = 0

        theChosenTableau = []
        theSecondChosenTableau = []
        leRetourDesTableau = []

        for j in range(0, len(allTabs)):
            for k in range (0, len(allTabs[j])):
                theChosenOne+=allTabs[j][k]
                if(theChosenOne >= index1):
                    theChosenTableau = allTabs[j]
                    break
            else:
                continue
            break
        for l in range(0, len(allTabs)):
            for m in range (0, len(allTabs[l])):
                theSecondChosenOne+=allTabs[l][m]
                if(theSecondChosenOne >= index2):
                    theSecondChosenTableau = allTabs[l]
                    break
            else:
                continue
            break
        leRetourDesTableau.append(theChosenTableau)
        leRetourDesTableau.append(theSecondChosenTableau)
        return leRetourDesTableau


    def copulation(tab1, tab2):
        tab3 = tab2[0] + tab2[1]
        #print tab3
        engeance = []
        i=0
        while i < len(tab2[0]):
            end = len(tab3)-1
            indx = randint(0,end)
            mutationPossible = randint(0,100)
            if mutationPossible > 3:
                engeance.append(tab3[indx])
            else:
                mutation = randint(0,10)
                engeance.append(mutation)
            del tab3[indx]
            i+=1
        ind1 = individu()
        ind1.setGenes(engeance)
        ind2 = individu()
        ind2.setGenes(tab3)
        return [ind1,ind2]