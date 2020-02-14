# 13.	Determine cuánto dinero hay en un banco que contiene 
# N1 billetes de 50000, 
# N2 billetes de 20000, 
# N3 billetes de 10000, 
# N4 billetes de 5000, 
# N5 billetes de 2000, 
# N6 billetes 1000, 
# N7 billetes de 500 y N8 billetes de 100.
TIPOS_BILLETES = {
	"Cincuentamil": 50000, 
	"Veintemil": 20000, 
	"Diezmil": 10000,
	"Cincomil": 5000,
	"Dosmil": 2000,
	"Mil": 1000,
	"Quinientos": 500,
	"Cien": 100
}

def pedirCantidadBilletes():
	cantidadTotal = 0
	while True:
		try:
			for billete, valor in TIPOS_BILLETES.items():
				cantidadTotal += int(input(f"ingrese la cantidad de billetes de {billete}: ")) * valor
				if(billete == "Cien"):
					print(f"La cantidad Total en el banco es de: {cantidadTotal} ")
					return True
		except ValueError:
			cantidadTotal = 0
			print("Vuelva a intentarlo de nuevo: ")


if __name__ == '__main__':
	pedirCantidadBilletes()