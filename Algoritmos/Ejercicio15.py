# 15.	Calcular y mostrar el monto total a pagar en un mes de luz eléctrica,
# teniendo  como dato la lectura anterior, la lectura actual y el costo por kilovatio.

def calcularReciboLuz(lecturaAnterior, lecturaActual, kilovatio):
	return (lecturaActual - lecturaAnterior) * kilovatio

def solicitarDatos():
	print('''Haremos el calculo de cuanto debe pagar de luz
		******************************************************''')

	lecturaAnterior = int(input("Ingresa la lectura Anterior: "))
	lecturaActual = int(input("Ingresa la lectura Anterior: "))
	costoByKilovatio = float(input("Ingresa el costo por Kilovatio: "))
	totalToPay = calcularReciboLuz(lecturaAnterior, lecturaActual, costoByKilovatio)
	print(f"El costo total a pagar en este mes es de: {totalToPay}")

if __name__ == '__main__':
	solicitarDatos()