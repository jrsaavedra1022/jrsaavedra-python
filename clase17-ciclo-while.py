import random

def run():
	number_found = False
	random_number = random.randint(0, 20)
	# print(random_number)

	while not number_found:
		number = int(input('Inserta un número: '))

		if number == random_number:
			print('Felicidades adivinaste el número')
			number_found = True
		elif number > random_number:
			print('El número es pequeño ')
		else: 
			print('El número es más grande')
	
i = 0
while i < 10:
 	print(i)
 	i += 1
		
if __name__ == '__main__':
	run()