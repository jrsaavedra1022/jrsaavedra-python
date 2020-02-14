# -*- coding: utf-8 -*-
def foreign_exchange_calculator(ammount):
	max_to_col_rate = 145.97
	return max_to_col_rate * ammount

def run():
	print('C A L C U L A D O R A   D E   D I V I S A S')
	print('Convierte de pesos Mexicanos a Colombianos')
	print('')

	ammount = float(input('Ingresa la cantidad de pesos Mexicanos que quieres convertir: '))

	result = foreign_exchange_calculator(ammount)
	print('${} pesos Mexicanos son ${} pesos Colombianos'. format(ammount, result))
	print('')

if __name__ == '__main__':
	run()
