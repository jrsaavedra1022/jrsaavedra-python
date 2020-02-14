# 20.	Calcule qué tanto por ciento anual cobraron por un 
# préstamo de Bolívares X, 
# si se pagaron Bolívares Y de intereses en 4 años. 
# La fórmula del interés es:
 

# I = ((Capital * Tiempo * Razón) / 100)

def calcularInteres(capital, tiempo, razon):
	razonSocial = razon / tiempo
	return (razonSocial * 100) / capital


def run():
	print('''		Bienvenido al BancoNacional
		**********************************
		Te ofrecemos un pago por dejar en nuestras manos tu dinero
		------------------------------------
		''')	
	tiempo = 4
	prestamo = float(input("Ingrese el valor del prestamo: "))
	razon = float(input("Ingrese la razon social (interes): "))
	interes = calcularInteres(prestamo, tiempo, razon)
	print("El porcentaje de ganancia anual del prestamo es de {}".format(interes))





if __name__ == '__main__':
	run()

