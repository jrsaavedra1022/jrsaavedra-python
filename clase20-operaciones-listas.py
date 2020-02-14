mi_lista = []
print(type(mi_lista))
mi_lista.append(1)

nueva_lista = [2, 3, 4]

mi_lista_suma = mi_lista + nueva_lista
print(mi_lista_suma)
mi_lista_multiplicacion = mi_lista * 10
print(mi_lista_multiplicacion)

ordenList = ["uno", "dos", "tres"]
print(ordenList)

print(ordenList[::-1])

# Modificacion de listas

ordenList[0] = "cero"
print(ordenList)

# eliminar el ultimo elemento de la lista
ordenList.pop()
print(ordenList)

#ordenar lista
listaDesorden = [4, 3, 7, 1]
print(listaDesorden)
listaDesorden.sort()
print(listaDesorden)
# eliminar elemento
utiles = ["lapiz", "borrador", "Tajalapiz", "esfero"]
print(utiles)
del utiles[0]
print(utiles)
# crear lista strings
casa = "casa"
lista_casa = list(casa)
print(lista_casa)
union_casa = ''.join(lista_casa)
print(union_casa)