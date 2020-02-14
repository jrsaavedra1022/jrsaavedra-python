# 10. El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente
# 100 chelines austríacos = 956.871 pesetas
# 1 dólar EEUU = 122.499 pesetas
# 100 dracmas griegos = 88.607 pesetas
# 100 francos belgas = 323.728 pesetas
# 1 franco francés = 20.110 pesetas
# 1 libra esterlina = 178.938 pesetas
# 100 liras italianas = 9.289 pesetas
# Lea una cantidad en chelines austriacos e imprima el equivalente en  pesetas.
# Lea una cantidad en dracmas griegos e imprima su  equivalente  en  francos franceses.
# Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.
def templateInicial():
	print('''
	:::::::::::::::::::::: SISTEMA DE CONVERSIONES (PESETA ADVANCED) ::::::::::::::::::::::::

	Haremos la conversión de monedas en las siguientes Esquivalencias
	   100 chelines austríacos = 956.871 pesetas
	   1 dólar EEUU = 122.499 pesetas
	   100 dracmas griegos = 88.607 pesetas
	   100 francos belgas = 323.728 pesetas
	   1 franco francés = 20.110 pesetas
	   1 libra esterlina = 178.938 pesetas
	   100 liras italianas = 9.289 pesetas
	''')

def templateOpcionesSistema():
	print('''
	****************************************************************************************
	   Opciones del sistema:
	   [A]  Empezar   ||   [B]  Salir   ||   [C]  Ver Menú   ||   [D]  Opciones del Sistema

	*****************************************************************************************  

	''')

def templateMenu():
	print('''
	Bienvenido al sistema de conversiones
	:::::::::: M E N U ::::::::::::::::::
	Opciones Menú de conversión:
	[CA]  Chelines Austríacos
	[DEU] Dólar EEUU
	[DG]  Dracmas Griegos
	[FB]  Francos Belgas
	[FF]  Franco Francés
	[LE]  Libra Esterlina
	[LI]  Libra Italianas
	[P]   Pesetas
	-------------------------------------------------
	''')

conversionesPesetas = {
	"CA": {"chelinAustriaco": 9586.71},
	"DEU": {"dolarEEUU": 122499},
	"DG": {"dracmaGriego": 886.07},
	"FB": {"francoBelga": 3237.28},
	"FF": {"francoFrances": 20110},
	"LE": {"libraEsterlina": 178938},
	"LI": {"liraItalina": 92.89},
	"P": {"pesetas": 1}
}

def doConvert(moneda, cantidadMonedad, monedaToConvert):
	print(sorted(conversionesPesetas[moneda].values())[0])
	pesetaInicial = sorted(conversionesPesetas[moneda].values())[0] * float(cantidadMonedad)
	pesetaFinal =  sorted(conversionesPesetas[monedaToConvert].values())[0]
	return pesetaInicial / pesetaFinal

def comenzarConversion():

	opcionInicialConversion = str(input('''Ingrese la monedad que desea convertir, dos puntos y el valor (Todo pegado).
		Ejemplo: CA:2500 \n'''))
	opcionConversion = opcionInicialConversion.split(":")[0]
	cantidadInicialConversion = opcionInicialConversion.split(":")[1]

	if opcionConversion in conversionesPesetas:
		opcionFinalConversion = str(input('''Ingrese la monedad a la cual deseas convertir:
		Ejemplo: FF \n'''))
		if opcionFinalConversion in conversionesPesetas:
			print(f'''La conversión será la siguiente:
			{cantidadInicialConversion} {sorted(conversionesPesetas[opcionConversion].keys())[0]} To {sorted(conversionesPesetas[opcionFinalConversion].keys())[0]} ''')
			cantidadFinal = doConvert(opcionConversion, cantidadInicialConversion, opcionFinalConversion)
			print(f"El resultado en es : {cantidadFinal}")
		else:
			print("Error esa opcion no Existe, Intenta Nuevamente ...")
				

	else:
		print("Error esa opcion no Existe, Intenta Nuevamente ...")

	return 1




def run():
	while True:
		templateOpcionesSistema()
		opcionInicial = str(input("Escriba una opcion del sistema: "))
		if opcionInicial == 'A':
			print("Ten en cuenta el menú de opciones \n")
			templateMenu()
			comenzarConversion()
		elif opcionInicial == 'B':
			break
		elif opcionInicial == 'C':
			templateMenu()
		else:
			print("No Existe esa opcion en el Menú")




templateInicial()
# templateOpcionesSistema()


run()




# print(conversionesPesetas.fromKeys())


# def convesionesMoneda(monedaToConvert, monedaConvert):
# reglaTres(monedaToConvert, monedaConvert)

# def chelinesPesetas(monedaToConvert):
# return (monedaToConvert * 100)/ 956871

# def dramasGriegosToFrancosFrances(monedaToConvert):
# pesetas = (monedaToConvert * 88607)/ 100
# return pesetas / 20110

# def pesetaToDolar(monedaToConvert):
# return monedaToConvert * 122499

# def pesetaToLiraItaliana(monedaToConvert):
# return (monedaToConvert * 9289)/ 100


# chelines = float(input("Ingrese la cantidad en chelines: "))
# pesetas = chelinesPesetas(chelines)
# print(f"La cantidad de pesetas en chelines es: {pesetas}")

# dragmasGriegos = float(input("Ingrese la cantidad en dragmas Griegos"))
# francosFranceses = dramasGriegosToFrancosFrances(dragmasGriegos)
# print(f"La cantidad de dramas griegos en francos franceses es: {francosFranceses}")

# pesetasCantidad = float(input("Ingrese la cantidad en pesetas "))
# dolares = pesetaToDolar(dragmasGriegos)
# liraItalina = pesetaToLiraItaliana(dragmasGriegos)
# print(f"La cantidad de pesetas en dolares es: {dolares} y en liras italianas es: {liraItalina}")
