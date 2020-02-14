# secuencias de range

# start => end => steps
number = range(5, 40, 3)
print(number)
print(list(number))

for i in range(5):
	print(i)

print("Elevar al cuadrado numero divisibles entre tres")
for i in range(30):
	if i % 3 != 0:
		continue
	else:
		print(i**2)

print("romper un ciclo con break")
for i in range(30):
	if i % 3 == 0:
		print(i**2)
	elif i == 22:
		break 

r = 'ferrocarril'

print("recorrer un string")
for letter in r:
	print(letter)