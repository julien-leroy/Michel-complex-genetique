from generation import generation
from individu import individu
from randm import randm

tabGen = []

def main():
	# for x in xrange(0,10):
	# 	nextGen()
	# 	print tabGen[x].tournament()
	# 	raw_input()
	
	gen = generation()
	#print gen.printPedro()
	fin1 = gen.tournament()
	print fin1()

	# print gen.getAllFitness()
	# fin2 = gen.copulation(fin1)
	# print fin2

def nextGen():
	print("gen numero : " + str(len(tabGen) + 1))
	tabGen.append(generation())

if __name__ == "__main__":
    main()