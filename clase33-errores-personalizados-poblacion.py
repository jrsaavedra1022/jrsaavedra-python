countries = {
	'mexico': 122,
	'colombia': 49,
	'argentina': 42,
	'chile': 10,
	'peru': 31
}

while True:
	country = str(input('Escribe el nombre del pais: ')).lower()
	try:
		print('La población de {} es: {} millones'.format(country, countries[country]))
	except KeyError:
		print('No tenemos la población del pais mencionado "{}"'.format(country))		