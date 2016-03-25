import math
from random import *

nameDictionary = [
    'are',
    'di',
    'mo',
    'fa',
    'dar',
    'kil',
    'glar',
    'tres',
    'fool',
    'por',
    'fuk',
    'nor',
    'rik',
    'toss',
    'mi',
    'zor',
    'kor',
    'ror',
    'toz',
    'root',
    'frooz',
    'cthu',
    'lu'
]

class Cthulhu:
	def __init__(self):
		self.initGenes()

	def initGenes(self):
		self.name = ""
		self.nameGenerator()
		self.score = 0

		self.apparence = randint(1,10)
		self.constitution = randint(1,10)
		self.dexterite = randint(1,10)
		self.force = randint(1,10)
		self.taille = randint(1,10)
		self.education = randint(1,10)
		self.intelligence = randint(1,10)
		self.pouvoir = randint(1,10)

		self.X = 0
		self.Y = 0
		self.Z = 0
		self.O = 0

		self.calculateForces()

		self.tabGenes = [self.apparence,self.constitution,self.dexterite,self.force,self.taille,self.education,self.intelligence,self.pouvoir]
		self.tabXYZOmega = [self.X,self.Y,self.Z,self.O]
		
		self.fitness()
		return self

	def calculateForces(self):
		self.X = self.forceAttraction()
		self.Y = self.scoreCombat()
		self.Z = self.planDominationMondiale()
		self.O = self.degatReveil()

	def forceAttraction(self):
		X = (math.pow(self.intelligence,2))*(math.exp(self.apparence*self.pouvoir))*self.education
		return X

	def scoreCombat(self):
		Y = (self.dexterite/self.taille)*math.pow(self.force,self.constitution/29.53)*math.sqrt(self.pouvoir)
		return Y

	def planDominationMondiale(self):
		Z = (self.pouvoir*math.pow(self.intelligence,2))/3
		return Z

	def degatReveil(self):
		O = math.pow(self.pouvoir,2)*math.pow(self.force,math.sqrt(self.taille))
		return O


	def fitness(self):
		scoreFA = 	(self.X/(1000*math.exp(100)))*100
		
		scoreC = 	(self.Y/68.9665771964)*100
		
		scorePDM = 	(self.Z/(1000/3))*100
		
		scoreDR =	(self.O/145304.0301899042756154396695723461665813451520972058264661)*100

		self.score = scoreFA+scoreC+scorePDM+scoreDR

	def setGenes(self, newGen):
		self.apparence = newGen[0]
		self.constitution = newGen[1]
		self.dexterite = newGen[2]
		self.force = newGen[3]
		self.taille = newGen[4]
		self.education = newGen[5]
		self.intelligence = newGen[6]
		self.pouvoir = newGen[7]
		self.tabGenes = [self.apparence,self.constitution,self.dexterite,self.force,self.taille,self.education,self.intelligence,self.pouvoir]
		self.calculateForces()
		self.fitness()
		#print self.score

	def rnmdz(self):
		liste = []
		for walrandDegorge in range(0,self.nbGenesInt):
			liste.append(randint(0,10))
		# print liste
		return liste

	def getGenes(self):
		return self.tabGenes

	def getXYZOmega(self):
		return self.tabXYZOmega

	def getFitness(self):
		return self.score

	def getName(self):
		return self.name

	def printCthulhu(self):
		print "name : " + str(self.getName()) + " | fitness : " + str(self.getFitness()) + " | genes : " + str(self.getGenes())

	def nameGenerator(self):
		first_part = nameDictionary[randint(0,len(nameDictionary)-1)]
		second_part = nameDictionary[randint(0,len(nameDictionary)-1)]

		self.name = first_part + second_part