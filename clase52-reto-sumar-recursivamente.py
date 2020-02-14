# sumar recursivamente los numero del 1 al 100


def run(suma=0):
	number = int(input("ingrese un número a sumar: "))
	sumaFinal = number + suma
	print("La suma es: {}".format(sumaFinal))
	number = run(sumaFinal)


if __name__ == '__main__':
	run()
