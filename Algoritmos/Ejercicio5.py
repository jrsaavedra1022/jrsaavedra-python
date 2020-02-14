# 5.	Un alumno desea saber cuál será su calificación final en la materia
#  de  computación.  Dicha calificación se compone de los siguientes porcentajes:
#  55%  del promedio de sus tres calificaciones parciales, 
#  30% de la calificación del exámen final y 
#  15% de la calificación de un trabajo final.
porcentajeNotas = 55
porcentajeExamen = 30
porcentajeTrabajoFinal = 15
print("ingrese las 3 notas del alumno: ")
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))
notaExamen = float(input("Ingrese nota del Examen: "))
notaTrabajoFinal = float(input("Ingrese nota del trabajo Final: "))

def calcularPromedio(nota, promedio):
	return (nota*promedio)/100

NotaFinal = calcularPromedio(((nota1+nota2+nota3)/3), porcentajeNotas) + calcularPromedio(notaExamen, porcentajeExamen) + calcularPromedio(notaTrabajoFinal, porcentajeTrabajoFinal)
print(f" La nota final del estudiante es: {NotaFinal}")