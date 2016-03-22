from cthulhu import *
from generation import *

def main():
	GG = Generation()
	C1 = Cthulhu()
	C2 = Cthulhu()

	f1 = Cthulhu()
	f2 = Cthulhu()
	# GG.printGen()

	tabEnfant = GG.copulation(C1,C2)
	f1.setGenes(tabEnfant[0])
	f2.setGenes(tabEnfant[1])

	f1.printCthulhu()
	f2.printCthulhu()


if __name__ == "__main__":
    main()