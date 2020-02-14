# 18.	Resuelva el problema que tienen en una gasolinera.
# Los surtidores de la misma registran lo que surten en galones, 
# pero el precio de la  gasolina está fijado en  litros. 
# Se requiere que calcule y muestre lo que hay que cobrarle a un cliente, considerando que: 
# (a) cada galón tiene 3.785 litros; 
# (b) el precio del litro es de 100 Bolívares.

def calcularTotalToPay(galones):
	litros = galones * 3785
	bolivares = litros * 100
	return bolivares


def run():
	cantidadGalones = float(input("Ingrese la cantidad en galones comprador por el cliente: "))
	TotalPago = calcularTotalToPay(cantidadGalones)
	print("El total a pagar en bolivares es de: {}".format(TotalPago))


if __name__ == '__main__':
	run() 