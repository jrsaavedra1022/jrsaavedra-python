# 19.	En un hospital rural existen tres áreas: Ginecología, Pediatría y Traumatología. 
# El presupuesto anual del hospital se reparte conforme a la siguiente tabla:

# Área	Porcentaje del presupuesto
# Ginecología	40%
# Traumatología	30%
# Pediatría	30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestado.

def calcularPorcentajeAreas(presupuesto):
	genecologia = (presupuesto * 40) / 100
	traumatologia = (presupuesto - genecologia) / 2
	pediatria = (presupuesto - genecologia) / 2
	print("El presupuesto del hospital {} se dividira de la siguiente manera: ".format(presupuesto))
	print("Ginecología: {}, Traumatología: {}, Pediatría: {}".format(genecologia, traumatologia, pediatria))  

def run():
	presupuesto =  float(input("Ingrese el presupuesto Total del hospital: "))
	calcularPorcentajeAreas(presupuesto)

if __name__ == '__main__':
	run()