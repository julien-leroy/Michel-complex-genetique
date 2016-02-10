from randm import *

class individu:

	def __init__(self):
		self.tabGenes = []
		self.score    = 0
		self.initGenes()
		self.fitness()

	def initGenes(self):
		self.tabGenes = self.rnmdz()
		return self

	def fitness(self):
		self.score = sum(self.tabGenes)
		return self

	def setGenes(self, newGen):
		self.tabGenes = newGen
		self.fitness()

	def rnmdz(self):
		liste = []
		for walrandDegorge in range(0,4):
			liste.append(randint(0,10))
		# print liste
		return liste

	def getGenes(self):
		return self.tabGenes

	def getFitness(self):
		return self.score
