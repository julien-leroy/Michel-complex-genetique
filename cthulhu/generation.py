from random import *
from cthulhu import *
import math

class Generation:
    def __init__(self, ioogyu):
        #On initialise la generation 
    	self.tabIndividus = self.initGeneration()
        self.ioogyu = ioogyu

    def initGeneration(self):
        tab = []
        #On cree une generation de 10 Cthulhus
        for y in range(0,10):
            tab.append(Cthulhu())
        return tab

    def printGen(self):
        #Cette fonction permet l'affichage de chaque individu dans la console, accompagne de son score et de son nom
    	tab2 = []
        for z in range(0,len(self.tabIndividus)):
            perso = self.tabIndividus[z]
            print "score : " + str(perso.getFitness()) + " | name : " + str(perso.getName()) + " | genes : " + str(perso.getGenes())
        print "Score moyen : " + str(self.getMoyenne())

    def getMoyenne(self):
        #On recupere la moyenne du score de tous les individus de la generation
        scoreMoyen = 0
        for z in range(0,len(self.tabIndividus)):
            scoreMoyen += self.tabIndividus[z].getFitness()
        scoreMoyen = scoreMoyen / len(self.tabIndividus)
        return scoreMoyen


    def getGen(self):
        #Permet de recuperer tous les individus de la generation
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
        #Permet de recuperer la somme des scores de toute la generation
        num = 0
        tab = self.tabIndividus
        for k in range(0, len(tab)):
            num += tab[k].getFitness()
        return num

    def getAllScoresTable(self):
        #Permet de recuperer le tableau des scores de la generation
        allScores = []
        for t in range(0, len(self.tabIndividus)):
            allScores.append(self.tabIndividus[t].getFitness())
        return allScores


    def RWS(self):
        #La technique RWS consiste a choisir aleatoirement dans une liste d individus 
        #dont le pourcentage de chance d etre choisi depend de leur fitness. C est la technique de la roue.

        allTabs = self.getGen() 
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
        #la fonction qui va creer 2 enfant avec les 2 parents choisis grace a la methode de selection. 
        #Ici pour chaque gene il y aura 49% de chance d avoir le gene de la mere,
        # 49% d avoir le gene du pere et 2% de chance de muter.
        maxtab = len(cthulhu1)
        genesC3 = []
        genesC4 = []
        i=0
        while i<maxtab:
            rand = randint(0,100)
            if rand<49:
                genesC3.append(cthulhu1[i])
                genesC4.append(cthulhu2[i])
            elif rand>=49 and rand<=98:
                genesC3.append(cthulhu2[i])
                genesC4.append(cthulhu1[i])
            else:
                #mutation 2%
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
        #La technique du tournament selectionne 2 individus pour confronter leur score et choisir le pere. 
        #La meme selection est faite pour la mere.
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
        #On recupere tous les scores de la generation et on en retire le meilleur
        allScores = self.getAllScoresTable()
        bestScore = 0

        for i in allScores:
            if i > bestScore:
                bestScore = i

        return bestScore

    
    def printIndicateurs(self):
        #On recupere les  statistiques de la generation
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

