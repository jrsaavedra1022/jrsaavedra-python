# 8.	Calcule el área de un triángulo en función de las longitudes de sus  lados,  
# utilizando la fórmula:	raiz de p(p­a)(p­b)(p­c) donde p = (a+b+c) / 2

import math

def raizCuadrada(cantidad):
	return math.sqrt(cantidad)

def calcularAreaTriangulo(DatosTringulo):
	p = DatosTringulo["P"]
	a = p - DatosTringulo["Lado1"]
	b = p - DatosTringulo["Lado2"]
	c = p - DatosTringulo["Lado3"]
		
	return raizCuadrada(p*a*b*c) 

def obtenerDatosTringulo():
	ladosTriangulo = {}
	cantidadTotal = 0
	while True:
		try:
			for i in range(3):
				if f"Lado{i+1}" not in ladosTriangulo:
					cantidad = float(input(f"Ingrese el lado del triángulo {i+1}: ")) 
					ladosTriangulo[f"Lado{i+1}"] = cantidad
					cantidadTotal += cantidad
			ladosTriangulo["P"] = cantidadTotal / 2 
			return ladosTriangulo
			break
		except ValueError:
			print("Error: tipo de dato invalido: !!")

DatosTringulo = obtenerDatosTringulo()
print(DatosTringulo)
AreaTringulo =  calcularAreaTriangulo(DatosTringulo)
print(f"El Área del tringulo es: {AreaTringulo}")