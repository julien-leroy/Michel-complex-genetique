from random import *
from cthulhu import *
import math

class Generation:
    def __init__(self, ioogyu):
    	self.tabIndividus = self.initGeneration()
        self.ioogyu = ioogyu

    def initGeneration(self):
        tab = []
        for y in range(0,10):
            tab.append(Cthulhu())
        return tab

    def printGen(self):
    	tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            print "score : " + str(perso.getFitness()) + " | name : " + str(perso.getName()) + " | genes : " + str(perso.getGenes())
        print "Score moyen : " + str(self.getMoyenne())

    def getMoyenne(self):
        scoreMoyen = 0
        for z in range(0,len(self.tabIndividus)):
            scoreMoyen += self.tabIndividus[z].getFitness()
        scoreMoyen = scoreMoyen / len(self.tabIndividus)
        return scoreMoyen


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
        num = self.getAllFitness()
        ScoresTable = self.getAllScoresTable()
        num = math.floor(num)
        index1 = randint(0, num)
        index2 = randint(0, num)

        theChosenOne = 0
        theSecondChosenOne = 0

        theChosenTableau = []
        theSecondChosenTableau = []
        leRetourDesTableau = []

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

        leRetourDesTableau.append(theChosenTableau)
        leRetourDesTableau.append(theSecondChosenTableau)
        return leRetourDesTableau



    def copulation(self, cthulhu1, cthulhu2):

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

        if self.ioogyu =="1":
            etape1 = self.RWS()
        else:
            etape1 = self.tournament()


        i = 0
        while i < len(self.tabIndividus)/2:

            C1 = Cthulhu()
            C2 = Cthulhu()

            etape1 = self.RWS()

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


    def bestScore(self):
        allScores = self.getAllScoresTable()
        bestScore = 0

        for i in allScores:
            if i > bestScore:
                bestScore = i

        return bestScore

    
    def printIndicateurs(self):
        allScores = self.getAllScoresTable()
        moy = sum(allScores) / len(allScores)
        i=0
        ret = 0
        while (i<len(allScores)):
            r=(allScores[i]-moy)**2
            ret += r
            i+=1
        variance = ret*(len(allScores)**(-1))
        ecartType = variance**0.5


        print("Moyenne : %s" %(moy))
        print("Variance : %s" %(variance))
        print("Ecart-type : %s" %(ecartType))
        print("Meilleur score : %s" %(self.bestScore()))

