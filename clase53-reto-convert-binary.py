
def decryptBinary_word(binaryElement):
	octetos = binaryElement.split(" ")
	contenido = ''
	for octeto in octetos:
		letter = bytearray(int(bit, 2) for bit in octeto.split())
		contenido += letter.decode(encoding="utf8")

	newWord = contenido
	print("La palabra o frase desencriptada es: ")
	print(newWord)

def encryptBinary_word(word):
	newWord = ' '.join(format(ord(character), 'b') for character in word)
	print("La palabra o frase encriptada es: ")
	print(newWord)

def request_of_message():
	while True:
		word = str(input("Escribe una frase o palabra: "))

		opcion = str(input('''
			Selecciona un opcion del menu:
				[e]ncriptar
				[d]esencriptar
			
			'''))
		if opcion.lower() == "e":
			encryptBinary_word(word)
		elif opcion.lower() == "d":
			decryptBinary_word(word)
		else:
			print("La opción del menu no existe")


if __name__ == '__main__':
	request_of_message()