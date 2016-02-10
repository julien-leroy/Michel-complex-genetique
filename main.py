from generation import generation
from individu import individu
from randm import randm

tabGen = []

def main():
	for x in xrange(0,10):
		nextGen()
		print tabGen[x].tournament()
		raw_input()
	
	#print gen 
	#print gen.printPedro()
	# print gen.RWS()

	# print gen.getAllFitness()

def nextGen():
	print("gen numero : " + str(len(tabGen) + 1))
	tabGen.append(generation())

if __name__ == "__main__":
    main()