from random import randint

def dice():
	return randint(1, 6)

for i in range(2):
	print(dice())