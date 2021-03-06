from random import *
from individu import individu
from randm import randm
import time

class generation:
    def __init__(self):
        self.tabIndividus = self.initGeneration()

    def initGeneration(self):
        tab = []
        for y in range(0,10):
            tab.append(individu())
        return tab

    def setTableauIndividus(self, ind):
        self.tabIndividus = ind

    def printGen(self):
        tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            persos = perso.getGenes()
            tab2.append(persos)
        return tab2

    def tournament(self):

        leRetourDesTableau = []
        
        def fight():

            rdn = randint(0, len(self.tabIndividus)-1)
            rdn2 = randint(0, len(self.tabIndividus)-1)
            
            indiv1 = self.tabIndividus[rdn]
            indiv2 = self.tabIndividus[rdn2]

            RWSTabs = [indiv1.getGenes(), indiv2.getGenes()]
            RWSFitness = indiv1.getFitness() + indiv2.getFitness()
            RWSIndex = randint(0, RWSFitness)
            theChosen = 0

            for j in range(0, len(RWSTabs)):
                for k in range (0, len(RWSTabs[j])):
                    theChosen+=RWSTabs[j][k]
                    # print("alltabsJK loop= ")
                    # print(allTabs[j][k])
                    # print("theChosen")
                    # print(theChosen)
                    if(theChosen >= RWSIndex):
                        theChosenTableau = RWSTabs[j]
                        #print("all tabs J")
                        #print RWSTabs[j]
                        break
                else:
                    continue
                break

            return theChosenTableau


        leRetourDesTableau.append(fight())
        leRetourDesTableau.append(fight())
        return leRetourDesTableau


    def getAllFitness(self):
        num = 0
        tab = self.tabIndividus
        for k in range(0, len(tab)):
            num += tab[k].getFitness()
        return num

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

    def moyenne(self,tableau):
        return sum(tableau, 0.0) / len(tableau)

    def variance(self,tableau):
        m=self.moyenne(tableau)
        return self.moyenne([(x-m)**2 for x in tableau])
    


