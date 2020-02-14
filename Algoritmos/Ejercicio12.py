# 12.	Calcule y muestre, a un alumno, cuál será su promedio general 
# en las  tres  materias más difíciles que cursa y 
# cuál será el promedio que obtendrá en cada    una de ellas. 
# Estas materias se evalúan como se muestra a continuación:
# Matemática		Examen 90% y	10% del promedio de tres tareas.
# Física		Examen 80% y	20% del promedio de dos tareas.
# Química		Examen 85% y	15% del promedio de tres tareas.

SUBJECT_DIFICULT = {
	"MATH": {"cantExams": 1, "promExams": 90, "cantHomeworks": 3, "promHomeworks": 10},
	"PHYSICAL": {"cantExams": 1, "promExams": 80, "cantHomeworks": 2, "promHomeworks": 20},
	"CHEMESTRY": {"cantExams": 1, "promExams": 85, "cantHomeworks": 3, "promHomeworks": 15}
}

print(''' 
{*********************************************************************}
Haremos el calculo de las tres materias más dificiles:
	Matemática 	Examen 90% y	10% del promedio de tres tareas.
	Física		Examen 80% y	20% del promedio de dos tareas.
	Química		Examen 85% y	15% del promedio de tres tareas.

{***********************************************************************}
	''')

def calcularPesoNota(nota, promedio):
	return (nota*promedio) / 100

def getPromExams(materia, cantidad, porcentaje, nombreStudent):
	notaFinalExam = 0
	for i in range(cantidad):
		notaFinalExam += float(input(f"Ingresa la nota {i+1} del examen de {materia} de {nombreStudent}: "))
	
	notaFinalExam = (notaFinalExam/cantidad)
	return calcularPesoNota(notaFinalExam, porcentaje)

def getPromHomeworks(materia, cantidad, porcentaje, nombreStudent):
	notaFinal = 0
	for i in range(cantidad):
		notaFinal += float(input(f"Ingresa la nota {i+1} de la tarea de {materia} de {nombreStudent}: "))
	
	notaFinal = (notaFinal/cantidad)
	return calcularPesoNota(notaFinal, porcentaje)


def pedirNotas():
	nombreStudent = str(input("Ingrese el nombre del estudiante: "))
	for subject, values in SUBJECT_DIFICULT.items():
		notaExamFinal = getPromExams(subject, values["cantExams"], values["promExams"], nombreStudent)
		notaHomeWorkFinal = getPromHomeworks(subject, values["cantHomeworks"], values["promHomeworks"], nombreStudent)
		notaFinal = notaExamFinal + notaHomeWorkFinal

		print(f"La nota final de {subject} es de: {notaFinal} \n")

	print(''' 
		************************************************
		 Gracias por usar nuestros servicios
		************************************************
		''')

if __name__ == '__main__':
	pedirNotas()