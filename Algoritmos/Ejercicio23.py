# 23.	Suponga que a partir de una Tonelada de maíz una planta productora obtiene 
# M kilogramos de harina y N litros de aceite. 
# La planta vende cada bulto de 24 paquetes de un kilogramo de harina en Bs. B1 y 
# cada caja de 15 envases de aceite  en Bs. B2. Suponiendo que la planta vende todo lo que  produce,  
# calcular  el  ingreso total por la venta de cada tonelada de maíz, 
# sabiendo además que cada kilogramo de harina y cada litro de aceite que restan del 
# embalaje se venden al  detal a los precios de Bs. B3 y Bs. B4 respectivamente. 
# Pruebe su algoritmo o programa con los sig. 
# Valores: M=452, N=197, B1=132, B2= 180, B3= 7,50 y B4= 14,50. Respuesta: 4895

def calcularValorGanancia(kilogramosHarina, litrosAceite, valorBultoHarina, valorCajaAceite, valorKilogramoHarina, valorLitroAceite):
	# calculo de harina
	cantidadBultos =  int(kilogramosHarina / 24)
	unidadesHarina = kilogramosHarina - (cantidadBultos * 24)  
	valorFinalBultoH = cantidadBultos * valorBultoHarina
	valorFinalHarina = unidadesHarina * valorKilogramoHarina   
	# calculo de aceite
	cantidadCajasAceite = int(litrosAceite / 15)
	unidadesLitrosAceite = litrosAceite - (cantidadCajasAceite * 15)
	valorFinalCajaAceite = cantidadCajasAceite * valorCajaAceite
	valorFinalAceite = unidadesLitrosAceite * valorLitroAceite

	# calculo final
	gananciaHarina =  valorFinalBultoH + valorFinalHarina
	gananciaAceite = valorFinalCajaAceite + valorFinalAceite
	return gananciaHarina + gananciaAceite



def run():
	print("Obteneremos la ganancia total")
	kilogramosHarina = float(input("Ingrese la cantidad de kilogramos de harina (452): "))
	litrosAceite = float(input("Ingrese los litros de aceite (197): "))
	valorBultoHarina = float(input("Ingrese el valor del bulto de harina (132): "))
	valorCajaAceite = float(input("Ingrese el valor del envase de aceite (180): "))
	valorKilogramoHarina = float(input("Ingrese el valor kilogramo de harina (7.50): "))
	valorLitroAceite = float(input("Ingrese el valor del litro de aceite (14.50): "))

	ganancia = calcularValorGanancia(kilogramosHarina, litrosAceite, valorBultoHarina, valorCajaAceite, valorKilogramoHarina, valorLitroAceite)
	print("La ganancia final es de: {}".format(ganancia))

	

if __name__ == '__main__':
	run()
