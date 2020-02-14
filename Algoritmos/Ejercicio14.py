# 14.	El siguiente sistema de ecuaciones lineales:
# aX + bY = c dX + eY = f
# se resuelve con las fórmulas:
# ce ­ bf	af ­ cd
# X= ­­­­­­­­­	Y=­­­­­­­­­­	calcule y muestre el valor de X e Y. Ae – bd		ae – bd

def calcularXandY(a,b,c,d,e,f):
	try:
		x = (c*e - b*f) / (a*e - b*d)
		y = (a*f - c*d) / (a*e - b*d)
		return {"x": x, "y": y}
	except ValueError:
		return 0

def calcularOpcionC(a,b,x,y):
	return a*x + b*y

def calcularOpcionF(d,e,x,y):
	return d*x + e*y

def pedirDatos():
	print("Haremos un calculo de ecuaciones lineales");
	try:	
		a = float(input("Ingrese el valor de a: "))
		b = float(input("Ingrese el valor de b: "))
		c = float(input("Ingrese el valor de c: "))
		d = float(input("Ingrese el valor de d: "))
		e = float(input("Ingrese el valor de e: "))
		f = float(input("Ingrese el valor de f: "))
		dataXY = calcularXandY(a,b,c,d,e,f)
		if dataXY != 0:
			print(f"El valor en x es: {dataXY['x']}")
			print(f"El valor en y es: {dataXY['y']}")
			print("Comprobamos !!!")
			print(f"El valor en c es: {calcularOpcionC(a, b, dataXY['x'], dataXY['y'])}")
			print(f"El valor en f es: {calcularOpcionF(d, e, dataXY['x'], dataXY['y'])}")
		else:
			print("Syntax Error div in zero !!")	

	except ValueError:
		print("Error intente de nuevo !!")
	

if __name__ == '__main__':
	pedirDatos()
