# Suponga que un individuo decide invertir su capital en un banco y 
# desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 2% mensual.
def calcular_porcentaje(capital, porcentajeMensual):
	return (capital*porcentajeMensual)/100

__PORCENTAJE_MENSUAL_BANCO = 2
ganaciaMensual = calcular_porcentaje(float(input("Ingrese el capital a calcular: ")), __PORCENTAJE_MENSUAL_BANCO)
print(ganaciaMensual)