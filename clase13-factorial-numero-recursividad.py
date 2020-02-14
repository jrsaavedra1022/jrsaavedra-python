#funciones factoriales
# 5! =>  5*4*3*2*1 
def factorial(number):
	if number == 0:
		return 1
	
	return number * factorial(number - 1)	

if __name__ == '__main__':
	number = int(input('Ingrese un número para factorial: '))

	result = factorial(number)

	print(f"El resultado del factorial de {number} es: {result}")