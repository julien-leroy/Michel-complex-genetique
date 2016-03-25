from random import *
from cthulhu import *
import math


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
        scoreMoyen = 0
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            scoreMoyen += perso.getFitness()
            print "score : " + str(perso.getFitness()) + " | name : " + str(perso.getName()) + " | genes : " + str(perso.getGenes())
        scoreMoyen = scoreMoyen / len(self.tabIndividus)
        print "score moyen : " + str(scoreMoyen)

    def getGen(self):
        allGenes = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            persos = perso.getGenes()
            allGenes.append(persos)
        return allGenes

    def setIndividus(self, newIndividus):
        self.tabIndividus = newIndividus
        return self

    def getAllFitness(self):
        num = 0
        tab = self.tabIndividus
        for k in range(0, len(tab)):
            num += tab[k].getFitness()
        return num

    def getAllScoresTable(self):
        allScores = []
        for t in range(0, len(self.tabIndividus)):
            allScores.append(self.tabIndividus[t].getFitness())
        return allScores


    def RWS(self):
        allTabs = self.getGen() # recuperation de tous les genes de la generation
        #print "allTabs: " + str(allTabs)
        num = self.getAllFitness()
        #print "num: " + str(num)
        ScoresTable = self.getAllScoresTable()
        num = math.floor(num)
        #print "num floored: " + str(num)
        index1 = randint(0, num)
        index2 = randint(0, num)

        theChosenOne = 0
        theSecondChosenOne = 0

        theChosenTableau = []
        theSecondChosenTableau = []
        leRetourDesTableau = []

        # for j in range(0, len(allTabs)):
        #     for k in range (0, len(allTabs[j])):
        #         theChosenOne+=allTabs[j][k]
        #         if(theChosenOne >= index1):
        #             theChosenTableau = allTabs[j]
        #             break
        #     else:
        #         continue
        #     break

        for j in range(0, len(ScoresTable)):
            theChosenOne+=ScoresTable[j]
            if(theChosenOne>=index1):
                theChosenTableau=allTabs[j]
                break
            else:
                continue
            break

        for l in range(0, len(ScoresTable)):
            theSecondChosenOne+=ScoresTable[l]
            if(theSecondChosenOne>=index2):
                theSecondChosenTableau=allTabs[l]
                break
            else:
                continue
            break

        # for l in range(0, len(allTabs)):
        #     for m in range (0, len(allTabs[l])):
        #         theSecondChosenOne+=allTabs[l][m]
        #         if(theSecondChosenOne >= index2):
        #             theSecondChosenTableau = allTabs[l]
        #             break
        #     else:
        #         continue
        #     break



        leRetourDesTableau.append(theChosenTableau)
        leRetourDesTableau.append(theSecondChosenTableau)
        #print "leRetourDesTableau" + str(leRetourDesTableau)
        return leRetourDesTableau



    def copulation(self, cthulhu1, cthulhu2):
        # cthulhu1 = cthulhu1.getGenes()
        # cthulhu2 = cthulhu2.getGenes()
        #print cthulhu1
        #print cthulhu2
        maxtab = len(cthulhu1)
        genesC3 = []
        genesC4 = []
        i=0
        while i<maxtab:
            rand = randint(0,100)
            if rand<47:
                genesC3.append(cthulhu1[i])
                genesC4.append(cthulhu2[i])
            elif rand>=47 and rand<=97:
                genesC3.append(cthulhu2[i])
                genesC4.append(cthulhu1[i])
            else:
                #mutation 3%
                genesC3.append(randint(1,10))
                genesC4.append(randint(1,10))
            i+=1
        tableauDes2bebes = [genesC3, genesC4]
        return tableauDes2bebes

    def CreateNewGen(self):
        newGen = []

        i = 0
        while i < len(self.tabIndividus)/2:

            C1 = Cthulhu()
            C2 = Cthulhu()

            etape1 = self.tournament()
            etape2 = self.copulation(etape1[0],etape1[1])

            C1.setGenes(etape2[0])
            C2.setGenes(etape2[1])

            newGen.append(C1)
            newGen.append(C2)

            i += 1

        return newGen

    def tournament(self):
        
        def fight():

            rdn = randint(0, len(self.tabIndividus)-1)
            rdn2 = randint(0, len(self.tabIndividus)-1)
            
            indiv1 = self.tabIndividus[rdn]
            indiv2 = self.tabIndividus[rdn2]

            if indiv1.getFitness() >= indiv2.getFitness():
                return indiv1.getGenes()
            else:
                return indiv2.getGenes()

        leTableauContenantLePereEtLaMere = []
        leTableauContenantLePereEtLaMere.append(fight())
        leTableauContenantLePereEtLaMere.append(fight())
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

    def bestScore(self):
        allScores = self.getAllScoresTable()
        bestScore = 0

        for i in allScores:
            if i > bestScore:
                bestScore = i

        return bestScore

    def printIndicateurs(self):
        allScores = self.getAllScoresTable()

        moy = sum(list(allScores)) / len(allScores)
        scoreCarre = [(indiv-moy)**2 for indiv in allScores]
        variance = sum(list(scoreCarre)) / len(scoreCarre)
        ecartType = variance**0.5

        print("moyenne : %s" %(moy))
        print("variance : %s" %(variance))
        print("ecart-type : %s" %(ecartType))
        print("meilleur score : %s" %(self.bestScore()))
