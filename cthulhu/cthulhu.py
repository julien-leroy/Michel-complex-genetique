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

		self.Apparence = randint(1,10)
		self.Constitution = randint(1,10)
		self.Dexterite = randint(1,10)
		self.Force = randint(1,10)
		self.Taille = randint(1,10)
		self.Education = randint(1,10)
		self.Intelligence = randint(1,10)
		self.Pouvoir = randint(1,10)

		self.X = self.forceAttraction()
		self.Y = self.scoreCombat()
		self.Z = self.planDominationMondiale()
		self.O = self.degatReveil()


		self.tabGenes = [self.Apparence,self.Constitution,self.Dexterite,self.Force,self.Taille,self.Education,self.Intelligence,self.Pouvoir]
		self.tabXYZOmega = [self.X,self.Y,self.Z,self.O]
		self.score    = sum(self.tabXYZOmega)
		
		self.fitness()
		return self

	def forceAttraction(self):
		X = (math.pow(self.Intelligence,2))*(math.exp(self.Apparence*self.Pouvoir))*self.Education
		return X

	def scoreCombat(self):
		Y = (self.Dexterite/self.Taille)*math.pow(self.Force,self.Constitution/29.53)*math.sqrt(self.Pouvoir)
		return Y

	def planDominationMondiale(self):
		Z = (self.Pouvoir*math.pow(self.Intelligence,2))/3
		return Z

	def degatReveil(self):
		O = math.pow(self.Pouvoir,2)*math.pow(self.Force,math.sqrt(self.Taille))
		return O


	def fitness(self):
		self.score = sum(self.tabGenes)
		return self

	def setGenes(self, newGen):
		self.tabGenes = newGen
		self.fitness()

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

	def nameGenerator(self):
		first_part = nameDictionary[randint(0,len(nameDictionary)-1)]
		second_part = nameDictionary[randint(0,len(nameDictionary)-1)]

		self.name = first_part + second_part