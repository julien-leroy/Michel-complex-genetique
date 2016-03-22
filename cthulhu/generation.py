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
            print "name : " + str(perso.getName()) + " | fitness : " + str(perso.getFitness()) + " | genes : " + str(perso.getGenes())

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



    def copulation(self, cthulhu1, cthulhu2):
        genesC1 = cthulhu1.getGenes()
        genesC2 = cthulhu2.getGenes()
        print genesC1
        print genesC2
        maxtab = len(genesC1)
        genesC3 = []
        genesC4 = []
        i=0
        while i<maxtab:
            rand = randint(0,100)
            if rand<47:
                genesC3.append(genesC1[i])
                genesC4.append(genesC2[i])
            elif rand>=47 and rand<=97:
                genesC3.append(genesC2[i])
                genesC4.append(genesC1[i])
            else:
                #mutation 3%
                genesC3.append(randint(1,10))
                genesC4.append(randint(1,10))
            i+=1
        tableauDes2bebes = [genesC3, genesC4]
        print tableauDes2bebes
        return tableauDes2bebes



    def tournament(self):

        leRetourDesTableau = []
        
        def fight():

            rdn = randint(0, len(self.tabIndividus)-1)
            rdn2 = randint(0, len(self.tabIndividus)-1)
            
            indiv1 = self.tabIndividus[rdn]
            indiv2 = self.tabIndividus[rdn2]

            if indiv1.getFitness() >= indiv2.getFitness():
                return indiv1
            else:
                return indiv2

            # RWSTabs = [indiv1.getFitness(), indiv2.getFitness()]
            # RWSFitness = indiv1.getFitness() + indiv2.getFitness()
            # RWSIndex = randint(0, RWSFitness)
            # theChosen = 0

            # print "RWSTabs" + str(RWSTabs)
            # print "RWSFitness" + str(RWSFitness)
            # print "RWSIndex" + str(RWSIndex)

            # for j in range(0, len(RWSTabs)):
            #     for k in range (0, RWSTabs[j]):
            #         theChosen+=RWSTabs[j]
            #         # print("alltabsJK loop= ")
            #         # print(allTabs[j][k])
            #         # print("theChosen")
            #         # print(theChosen)
            #         if(theChosen >= RWSIndex):
            #             theChosenCreature = RWSTabs[j]
            #             #print("all tabs J")
            #             #print RWSTabs[j]
            #             break
            #     else:
            #         continue
            #     break

            # return theChosenCreature


        leTableauContenantLePereEtLaMere.append(fight())
        leTableauContenantLePereEtLaMere.append(fight())
        print leTableauContenantLePereEtLaMere
        return leTableauContenantLePereEtLaMere


        #print mitosis
        # engeance = []
        # i=0
        # while i < len(tab2[0]):
        #     end = len(mitosis)-1
        #     indx = randint(0,end)
        #     mutationPossible = randint(0,100)
        #     if mutationPossible > 3:
        #         engeance.append(mitosis[indx])
        #     else:
        #         mutation = randint(0,10)
        #         engeance.append(mutation)
        #     del mitosis[indx]
        #     i+=1
        # ind1 = individu()
        # ind1.setGenes(engeance)
        # ind2 = individu()
        # ind2.setGenes(mitosis)
        # return [ind1,ind2]