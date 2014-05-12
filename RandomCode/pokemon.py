"""
Pokeman catchign algorithm

"""

import random

	PB = "Pokeball"
	GB = "Greatball"
	UB = "Ultraball"
	SB = "Superball"
	MB = "Masterball"

	A = "Asleep"
	B = "Burned"
	PO = "Poisoned"
	PAR = "Paralyzed"
	FR = "Frozen"

def catch(pokeball, hp, status):

	#Pokeball 
	if pokeball == PB:
		r1 = random.randit(0,255)
	elif pokeball == GB:
		r1 = random.randit(0,200)
	else:
		r1 = random.randit(0,150)


	#Status variable
	if status == A || status == FR:
		s = 25
	elif status == PO || status == B || status == PAR:
		s = 20
	else:
		s = 0

	rStar = r1 - s

	if rStar < 0:
		print("caught")
		return

	#HP Factor 
	F = hp * 255
	if (F / 4 > 0):
		if (F/4 > 255):
			F = 255
		else:
			F = F / 4

	#Breaks free

	#





