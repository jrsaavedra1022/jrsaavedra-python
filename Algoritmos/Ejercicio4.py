# 4.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
# desea saber cuánto deberá pagar finalmente por su compra.
__DESCUENTO = 15
def generarDescuento(tatalCompra, descuento):
	return tatalCompra - ((tatalCompra * descuento)/100)

total = generarDescuento(float(input("Total de la compra: ")), __DESCUENTO)

print(f"El total a pagar es: {total}")