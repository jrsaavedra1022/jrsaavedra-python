# 7.	Dada una cantidad en metros, 
# se requiere que la convierta a pies y pulgadas, 
# considerando lo siguiente: 1 metro = 39.27 pulgadas; 1 pie = 12 pulgadas.

def convercionMetroToPulgada(metros):
	return metros * 39.27

def convercionMetroToPie(metros):	
	return convercionMetroToPulgada(metros) / 12

def obtenerCantidadMetros():
	while True:
		try:
			metros = int(input("Ingrese la cantidad en Metros: "))
			return metros
			break
		except ValueError:
			print("Opss !! lo sentimos tipo de dato invalido !!")		


metros = obtenerCantidadMetros()
print(f"La {metros} metros en pulgadas es: {convercionMetroToPulgada(metros)}")
print(f"La {metros} metros en pies es: {convercionMetroToPie(metros)}")
