# 21.	Un mayorista compra a un agricultor un lote de X naranjas a Bs. Y la docena. 
# Después de vender todas las naranjas a los detallistas, obtiene Bs. K. 
# Calcular el porcentaje de ganancia obtenida en la inversión. 
# Pruebe su programa con los siguientes valores: X=48000, Y=6, K=42000 para obtener 75% como resultado.

def obtenerPorcentajeGanacia(cantidadNaranjas, valorDocena, valorFinalObtenido):
	cantidadDocenas = cantidadNaranjas / 12
	valorFinalDocenas = cantidadDocenas * valorDocena
	ganancia = valorFinalObtenido - valorFinalDocenas
	porcentajeGanancia =  (ganancia * 100) / valorFinalDocenas
	return porcentajeGanancia


def run():
	while True:
		try:
			cantidadNaranjas = int(input("Ingrese la cantidad de naranjas: "))
			valorDocena = int(input("Ingrese el valor de la docena: "))
			valorFinalObtenido = int(input("Ingrese el valor final obtenido: "))
			porcentaje = obtenerPorcentajeGanacia(cantidadNaranjas, valorDocena, valorFinalObtenido)

			print("El porcentaje de ganancia fue de: {}%".format(porcentaje))
			
		except ValueError:
			print("Error de sintaxis")
		


if __name__ == '__main__':
	run()