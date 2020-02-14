class Activity:
	def __init__(self, code, name, startTime, endTime, date, description):
		self.uid = code
		self.name = name
		self.startTime = startTime
		self.endTime = endTime
		self.date = date
		self.description = description
		self.state = 'Activo'

class Cronograma:
	

	def __init__(self):
		self._activityRequired = []

	def consultActity(self, name):
		for activity in self._activityRequired:
			if activity.name.lower() == name.lower():
				self._print_activity(activity)
			else:
				print("No existe")

	def _print_activity(self, activity):
		print("\n--- La actividad es: ")
		print("name: {}".format(activity.name))
		print("hora inicio: {}".format(activity.startTime))
		print("hora fin: {}".format(activity.endTime))
		print("fecha: {}".format(activity.date))
		print("descripcion: {}".format(activity.description))


	def requuestData(self):
		print('''
			Bienvenido al cronograma de actividades !!!
			''')
		code = int(input("Ingrese el codigo de la actividad: "))
		name = str(input("Ingrese el nombre de la actividad: "))
		start = str(input("Ingrese la hora inicio de la actividad: "))
		end = str(input("Ingrese la hora fin de la actividad: "))
		date = str(input("Ingrese la fecha de la actividad: "))
		description = str(input("Ingrese la descripcion de la actividad: "))
		a = Activity(code, name, start, end, date, description)
		self._activityRequired.append(a)



if __name__ == '__main__':
	act = Cronograma()
	act.requuestData()
	act.consultActity("cantar")
