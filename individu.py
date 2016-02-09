from randm import *

class individu:

	def __init__(self):
		self.tabGenes = []
		self.score    = 0

	def initGenes(self):
		self.tabGenes = self.rnmdz()
		return self

	def fitness(self):
		self.score = sum(self.tabGenes)
		return self

	def create(self):
		self.initGenes()
		self.fitness()
		return self

	def rnmdz(self):
		liste = []
		for y in range(0,5):
			liste.append(randint(0,10))
		# print liste
		return liste

	def getGenes(self):
		return self.tabGenes

	def getFitness(self):
		return self.score
