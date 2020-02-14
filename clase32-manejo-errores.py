# link de errores
# https://docs.python.org/3.5/reference/compound_stmts.html#try
# try => código que puede contener error
# except => posible tipo de error 
# else => si no sucede ningun error
# finally => ejecuta siempre sin importar los que suceda


def run_exceptions(number1, number2):
	resultado = 0
	try:
		resultado =  number1 / number2
		print("El resultado es: {}".format(resultado))
	except Exception as e:
		print(f"error except: {e}")
	else:
		print("Else: continueamos con el siguiente paso")
	finally:
		print("Final de proceso independientemente de lo que suceda")

if __name__ == '__main__':
	print(":::::::::::::: validaciones de error ::::::::::::::::::")
	run_exceptions(5, 3)
