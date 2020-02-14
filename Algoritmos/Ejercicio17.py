# 17.	Dados como datos el precio final pagado por un producto 
# y su precio de venta al público (PVP), 
# se requiere que calcule y muestre el porcentaje de descuento que le ha sido aplicado.

def calcularDescuento(pvp, precioFinal):
	if pvp <= precioFinal:
		print("No se ha aplicado descuento")
	else:
		porcentajeDescuento = (100 * precioFinal) / pvp
		porcentajeDescuento = 100 - porcentajeDescuento
		print("El descuento de su compra fue del: {}".format(porcentajeDescuento))

def run():
	valorProductoPublico = float(input("Ingrese el valor del producto público: "))
	valorFinalProducto = float(input("Ingrese el valor final del producto: "))
	calcularDescuento(valorProductoPublico, valorFinalProducto)


if __name__ == '__main__':
	run()