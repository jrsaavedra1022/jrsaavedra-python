# 9.	Calcular el salario neto de un trabajador en función
#  del número de horas trabajadas, el precio de la hora
#   y considerando un descuento fijo 
#   al sueldo base    por concepto de impuestos del 20%.

__SUELDO_BASE = 800000
__DESCUENTO = 20


def calcular_sueldoTrabajador(nHorasTrabajadas, precioHora):
	descuento = __SUELDO_BASE - ((__SUELDO_BASE * 20)/100)
	sueldoAdicional = nHorasTrabajadas * precioHora
	return sueldoAdicional + descuento


print("Haremos el calculo de un sueldo de un trabajador")
horas = int(input("Ingrese el cuantas Horas tiene el trabajador "))
precioHora = int(input("Ingrese el precio del trabajador "))

calculoFinal = calcular_sueldoTrabajador(horas, precioHora)
print(f"El sueldo final del trabajador es: {calculoFinal}")
