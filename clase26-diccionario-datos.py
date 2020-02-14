#diccionarios
# otherDiccionario = dict()
mi_diccionario = {}
mi_diccionario['firstElement'] = "Hola"
mi_diccionario['secondElement'] = "Adios"


print(mi_diccionario['firstElement'])
calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['programingWeb'] = 8
calificaciones['dataBase'] = 10

# imprimir llaves
for key in calificaciones:
	print(key)

# imprimir valores
for values in calificaciones.values():
	print(values)

# imprimir llave y valor
for key, value in calificaciones.items():
	print("Llave: {} valor: {}".format(key, value)) 

# promedio calificaciones
def promedio(calificaciones):
	suma_de_calificaciones = 0
	for calificacion in calificaciones.values():
		suma_de_calificaciones += calificacion

	return suma_de_calificaciones / len(calificaciones.values())

resultado = promedio(calificaciones)
print("La suma de calificaciones es {} ".format(resultado))