from random import *
from individu import individu
from randm import randm

class generation:
    def __init__(self):
        self.tabIndividus = self.initGeneration()

    def initGeneration(self):
        tab = []
        for y in range(0,10):
            tab.append(individu())
        return tab

    def printGen(self):
        tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            persos = perso.getGenes()
            tab2.append(persos)
        return tab2

    def tournament(self):
        allTabs = self.printGen()

        print allTabs

        # leRetourDesTableau.append(theChosenTableau)
        # leRetourDesTableau.append(theSecondChosenTableau)
        # return leRetourDesTableau

    def getAllFitness(self):
        num = 0
        tab = self.tabIndividus
        for k in range(0, len(tab)):
            num += tab[k].getFitness()
        return num

    def RWS(self):
        # print sum(self.printPedro())
        # num = 0
        # tab = self.tabIndividus
        # for k in range(0, len(tab)):
        #     print tab[k].getFitness()
        #     num += tab[k].getFitness()
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
                # print("alltabsJK loop= ")
                # print(allTabs[j][k])
                # print("theChosenOne")
                # print(theChosenOne)
                if(theChosenOne >= index1):
                    theChosenTableau = allTabs[j]
                    print("all tabs J")
                    print allTabs[j]
                    break
            else:
                continue
            break

        for l in range(0, len(allTabs)):
            for m in range (0, len(allTabs[l])):
                theSecondChosenOne+=allTabs[l][m]
                # print("alltabsLM loop= ")
                # print(allTabs[l][m])
                # print("theSecondChosenOne")
                # print(theSecondChosenOne)
                if(theSecondChosenOne >= index2):
                    theSecondChosenTableau = allTabs[l]
                    print("all tabs L")
                    print allTabs[l]
                    break
            else:
                continue
            break
        leRetourDesTableau.append(theChosenTableau)
        leRetourDesTableau.append(theSecondChosenTableau)
        return leRetourDesTableau