from generation import generation
from individu import individu
from randm import randm

def main():
	gen = generation()
	#print gen 
	#print gen.printPedro()
	fin1 = gen.RWS_()
	print gen.RWS_()
	# print gen.getAllFitness()
	fin2 = gen.copulation(fin1)
	print fin2

if __name__ == "__main__":
    main()