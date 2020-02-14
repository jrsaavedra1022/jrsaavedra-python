# 22.	Un comerciante de computadores ofrece P precio por compra al contado ó 12 cuotas 
# de T Bolívares cada una. Desarrolle un programa para calcular 
# y mostrar cuál es el porcentaje que se cobra por el recargo en el pago del computador por cuotas.


def calcularPorcentajeRecargoProducto(valorInicial, valorCoutas):
	valorFinalCoutas = valorCoutas * 12
	valorFinalCoutas = (valorFinalCoutas * 100) / valorInicial
	return valorFinalCoutas - 100 
def run():
	while True:
		try:
			print("Sistema de obtencio de recarga en coutas")
			valorProducto = float(input("Ingrese el valor total del producto: "))
			valorCoutaMensual = float(input("Ingrese el valor de la couta en un periodo de 12 meses para el producto: "))
			porcentajeRecargo = calcularPorcentajeRecargoProducto(valorProducto, valorCoutaMensual)
			print("El porcentaje del recargo es de: {}%".format(porcentajeRecargo))
		except ValueError:
			print("Error tipo de datos !!")

if __name__ == '__main__':
	run()