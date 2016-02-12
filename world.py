from generation import generation
from individu import individu
from randm import randm
import numpy as np
class world:

    azeret = raw_input('Number of generations ?  ')
    nbGenerations =int(azeret) #doit etre pair
    RWSusage = raw_input('RWS (1) or Tournament (else) ?  ')
    
    genInit = generation()

    def __init__(self):
        self.initWorld()


    def initWorld(self):
        n=0
        allFitness = []
        allFitnessAverage = 0
        Variance0 = []
        while n < len(self.genInit.tabIndividus):
            print(self.genInit.tabIndividus[n].getGenes())
            n+=1
        for y in range(0,self.nbGenerations):
            tab = []
            allFitness.append(self.genInit.getAllFitness())
            allFitnessAverage += self.genInit.getAllFitness()
            for m in range(0, len(self.genInit.tabIndividus)-1):
                Variance0 += self.genInit.tabIndividus[m].tabGenes
                Variance1 = self.genInit.variance(Variance0)
            print("Gen number: " + str(y) + "  Variance: " + str(Variance1))
            i=0
            #print ("allFitness: " +str(allFitness))
            while i < len(self.genInit.tabIndividus)/2:
                #print len(self.genInit.tabIndividus)
                if(self.RWSusage == "1"):
                    etape1 = self.genInit.RWS()
                else:
                    etape1 = self.genInit.tournament()
                etape2 = self.genInit.copulation(etape1)
                tab.append(etape2[0])
                tab.append(etape2[1])
                print(str(tab[i].getGenes()) + " Fitness: " + str(tab[i].getFitness()))
                i+=1
            self.genInit.setTableauIndividus(tab);

        print("Avergage fitness: " + str(allFitnessAverage/(y+1)/len(self.genInit.tabIndividus)))


    def moyenne(self,tableau):
        return sum(tableau, 0.0) / len(tableau)

    def variance(self,tableau):
        m=self.moyenne(tableau)
        return self.moyenne([(x-m)**2 for x in tableau])
    
