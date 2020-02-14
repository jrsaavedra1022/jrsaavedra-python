# 6.	Un maestro desea saber qué porcentaje de 
# hombres y qué porcentaje de mujeres hay 
# en un grupo de estudiantes.
__typePopulation = ["Mujeres", "Hombres"]

def calcularPorcentaje(total, value):
	return (value * 100) / total

def obtener_cantidad_personas(TypePopulation):
	cantidadGroup = {}
	cantidadTotal = 0
	while True:
		try:
			for population in TypePopulation:
				if population not in cantidadGroup:
					cantidad = int(input(f"Por favor ingrese el número de {population}: "))
					cantidadGroup[population] = cantidad 
					cantidadTotal += cantidad
			cantidadGroup["Total"] = cantidadTotal
			return cantidadGroup	
			break
		except ValueError:
			print("Oops! El tipo de datos debe ser Entero. Intente nuevamente...")

def calcular_promedio_personas(groupPeople):
	while True:
		try:
			for persona in groupPeople:
				if "Total" in groupPeople:
					porcentaje = calcularPorcentaje(groupPeople["Total"], groupPeople[persona])
					print(f"El porcentaje de {persona} es: {porcentaje}")
			break
		except ValueError:
			print("Error de calculo ...")


groupPeople = obtener_cantidad_personas(__typePopulation)
calcular_promedio_personas(groupPeople)



