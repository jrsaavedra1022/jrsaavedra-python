# -+- coding: utf-8 -*-

from clase36-modelar-objeto import Lamp 

def run():
	lamp = Lamp(is_turned_on = True)

	while True:
		command = str(input('''
		¿Qué deseas hacer?

		[p]render
		[a]pagar
		[s]alir
		''')).lower()

		if command == 'p':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break 


if __name__ == '__main__':
	run()