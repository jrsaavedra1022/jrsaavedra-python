# 10.	El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente 
# 100 chelines austríacos	=	956.871 pesetas
# 1 dólar EEUU	=	122.499 pesetas
# 100 dracmas griegos =	88.607 pesetas
# 100 francos belgas	=	323.728 pesetas
# 1 franco francés	=	20.110 pesetas
# 1 libra esterlina	=	178.938 pesetas
# 100 liras italianas	=	9.289 pesetas
# Lea una cantidad en chelines austriacos e imprima el equivalente en  pesetas. 
# Lea una cantidad en dracmas griegos e imprima su  equivalente  en  francos franceses. 
# Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.


print("Haremos la conversión de monedas")
print(" 100 chelines austríacos	=	956.871 pesetas");
print(" 1 dólar EEUU	=	122.499 pesetas");
print(" 100 dracmas griegos =	88.607 pesetas");
print(" 100 francos belgas	=	323.728 pesetas");
print(" 1 franco francés	=	20.110 pesetas");
print(" 1 libra esterlina	=	178.938 pesetas");
print(" 100 liras italianas	=	9.289 pesetas");



def convesionesMoneda(monedaToConvert, monedaConvert):
	reglaTres(monedaToConvert, monedaConvert)

def chelinesPesetas(monedaToConvert):
	return (monedaToConvert * 100)/ 956871 

def dramasGriegosToFrancosFrances(monedaToConvert):
	pesetas = (monedaToConvert * 88607)/ 100 
	return pesetas / 20110

def pesetaToDolar(monedaToConvert):
	return monedaToConvert * 122499 

def pesetaToLiraItaliana(monedaToConvert):
	return (monedaToConvert * 9289)/ 100 

	
chelines = float(input("Ingrese la cantidad en chelines: "))
pesetas = chelinesPesetas(chelines)
print(f"La cantidad de pesetas en chelines es: {pesetas}")

dragmasGriegos = float(input("Ingrese la cantidad en dragmas Griegos"))
francosFranceses = dramasGriegosToFrancosFrances(dragmasGriegos)
print(f"La cantidad de dramas griegos en francos franceses es: {francosFranceses}")

pesetasCantidad = float(input("Ingrese la cantidad en pesetas "))
dolares = pesetaToDolar(dragmasGriegos)
liraItalina = pesetaToLiraItaliana(dragmasGriegos)
print(f"La cantidad de pesetas en dolares es: {dolares} y en liras italianas es: {liraItalina}")


