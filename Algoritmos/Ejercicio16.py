# 16.	Una empresa X trabaja con láminas de hierro para fabricar una pieza. 
# Se conoce que (a) la lámina mide en promedio 
# 4 metros de largo por 
# 1.5 metros de ancho; (b) 
# la pieza a fabricar consume 0.5 metros en total. 
# Se requiere que calcule y muestre cuántas piezas se fabrican con una lámina y cuánto será el desperdicio.
class Laminas:
	_AnchoLamina = 4
	_AltoLamina = 1.5
	_Pieza = 0.5

	def __init__(self):
		pass
	def calcular_residuo_and_piezas(self):
		piezas = self._calcular_cantidad_piezas()
		residuo = self._obtener_residuo(piezas)
		print("Las piezas son. {} y el residuo es: {} ".format(piezas, residuo))

	def _calcular_cantidad_piezas(self):
		totalLamina = self._AnchoLamina * self._AltoLamina
		totalPieza = self._Pieza ** 2
		return totalLamina / totalPieza

	def _obtener_residuo(self, piezas):
		return piezas - int(piezas)

def calcular_laminas():
	pieza = Laminas()
	pieza.calcular_residuo_and_piezas()

if __name__ == '__main__':
	calcular_laminas()