from generation import generation
from individu import individu
from randm import randm
import world
from time import strftime
from datetime import datetime

def main():
<<<<<<< HEAD
=======

	gen = generation()

	print gen.tournament()

	# ww = world.world()
	# for x in xrange(0,10):
	# 	nextGen()
	# 	#print tabGen[x].tournament()
	# 	raw_input()
>>>>>>> 6f816c6c70b8f51a5509579bd338ecc432715d63
	
	t01 = datetime.now()
	t1 = t01.strftime("%H:%M:%S.%f")
	ww = world.world()
	t02 = datetime.now()
	t2 = t02.strftime("%H:%M:%S.%f")
	print ("Start time: " + str(t1))
	print ("End time: " + str(t2))
	t03 = t02-t01
	#t3 = t03.strftime("%H:%M:%S.%f")
	print ("Elapsed time: " + str(t03))

	if(ww.RWSusage =="1"):
		print("Method used: RWS")
	else:
		print("Method used: Tournament")

	print("Number of generations: " + str(ww.nbGenerations))
	
if __name__ == "__main__":
    main()