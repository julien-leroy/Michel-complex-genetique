from generation import generation
from individu import individu
from randm import randm

class world:

    nbGenerations =1000 #doit etre pair
    #nbIndividuals = 20
    genInit = generation()

    def __init__(self):
        self.initWorld()


    def initWorld(self):
        n=0
        while n < len(self.genInit.tabIndividus):
            print(self.genInit.tabIndividus[n].getGenes())
            n+=1
        for y in range(0,self.nbGenerations):
            print("gen numero : " + str(y))
            tab = []
            i=0
            while i < len(self.genInit.tabIndividus)/2:
                #print len(self.genInit.tabIndividus)
                etape1 = self.genInit.RWS()
                etape2 = self.genInit.copulation(etape1)
                tab.append(etape2[0])
                tab.append(etape2[1])
                print(str(tab[i].getGenes()))
                i+=1
            self.genInit.setTableauIndividus(tab);



    def nextGen():
        print("gen numero : " + str(len(tabGen) + 1))
        tabGen.append(generation())

