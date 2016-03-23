from cthulhu import *
from generation import *

class World:

    genInit = Generation()
    print genInit.tabIndividus

    def __init__(self):
        self.initWorld()

    def initWorld(self):
        i=0
        while i < len(self.genInit.tabIndividus)/2:
            tab = []
            #tab.append(self.genInit.copulation(self.genInit.tabIndividus[0],self.genInit.tabIndividus[1]))
            etape1 = self.genInit.RWS()
            print "etape1: " + str(etape1)
            #print "etape1" + str(etape1)
            etape2 = self.genInit.copulation(etape1[0],etape1[1])
            #tab.append(etape2[0])
            #tab.append(etape2[1])	
            tab.append(etape2[0])
            tab.append(etape2[1])
            print "TAB TAB TAB" + str(tab)
            i+=1