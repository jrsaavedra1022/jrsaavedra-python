import subprocess

def calcularHoraExtra(extraHour, priceHour):
	return extraHour * (priceHour + ((priceHour * 25) / 100))

def paroForzoso(sueldoBase):
	return (sueldoBase * 5) / 100

def politicaHabitacional(sueldoBase):
	return (sueldoBase * 2) / 100

def cajaAhorro(sueldoBase):
	return (sueldoBase * 7) / 100

def subsidioHijos(cantidadHijos):
	return 17300 * cantidadHijos

def primaHogar(cantidadHijos):
	if cantidadHijos > 0:
		return 18000
	else:
		return 0
def actualizacionAcademica(bool):
	if bool == "SI":
		return 25000
	else: 
		return 0
def obtenerDiccionarioReport(keys, data):
	employee = {}
	for key in range(len(keys)):
		k = keys[key]
		employee[k] = data[key]
	
	return employee


# def exportReport(DATA_END, LLAVES):
 
# 	with open('Files/report-final-employee.csv', 'w') as csvfile:
# 		fieldnames = LLAVES
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
# 		writer.writeheader()
# 		writer.writerows(DATA_END)
	 
# 	print("Ha sido generado el reporte correctamente !!")


def exportReport(DATA_END, LLAVES):
	fileReport = open('Files/report-final-employee.csv', 'w')
	
	for i in range(len(DATA_END) + 1):
		if i == 0:
			cadena = ";".join(LLAVES)
			fileReport.write(cadena+ '\n')
		else:
			WORDS = []
			for key, values in DATA_END[i-1].items():
				WORDS.append(str(values))
			cadena = ";".join(WORDS)
			fileReport.write(cadena+ '\n')

	fileReport.close()
	subprocess.Popen(["start", "excel.exe", "Files/report-final-employee.csv"], shell=True)
	# archivo = open("hello.txt", “w”) 
	print("Ha sido generado el reporte correctamente !!")
	

def generarReportWork(DATAWORK, LLAVES):
	NEW_KEYS = LLAVES
	keySalary = ['sueldo-base', 'valor-horas-extra', 'paro-forzoso', 'politica-habitacional', 'caja-ahorro', 'Total-deduccion', 'sub-actualizacion-academica', 'subsidio-hijos', 'prima-hogar', 'Total-subsidio', 'Sub-Total', 'Sueldo-Final']
	NEW_KEYS += keySalary 
	DATA_EXPORT = DATAWORK
	contador = 0
	for employee in DATAWORK:
		valorHora = float(employee["ValorH"]) 
		extraHour = int(employee["NHextras"])
		cantidadHijos = int(employee["cant.H"])
		SUELDOBASE = int(employee["Htrabajadas"]) * valorHora
		VALOR_HORAS_EXTRA = calcularHoraExtra(extraHour, valorHora);
		# deducir
		PARO_FORZOSO = paroForzoso(SUELDOBASE)
		POLITICA_HABITACIONAL = politicaHabitacional(SUELDOBASE)
		CAJA_AHORRO = cajaAhorro(SUELDOBASE)
		TOTAL_DEDUCCION = PARO_FORZOSO + POLITICA_HABITACIONAL + CAJA_AHORRO
		#subsidios
		ACTUALIZACION_ACADEMICA = actualizacionAcademica(employee["A-academica"])
		SUBSIDIO_HIJOS = subsidioHijos(cantidadHijos)  
		PRIMA_HOGAR = primaHogar(cantidadHijos)  
		TOTAL_SUBSIDIO = ACTUALIZACION_ACADEMICA + SUBSIDIO_HIJOS + PRIMA_HOGAR
		#subTOTAL
		SUB_TOTAL = SUELDOBASE + VALOR_HORAS_EXTRA + TOTAL_SUBSIDIO
		#sueldo Final 
		SUELDO_FINAL = SUB_TOTAL - TOTAL_DEDUCCION 
		
		employeeSueldo = [SUELDOBASE, VALOR_HORAS_EXTRA, PARO_FORZOSO, POLITICA_HABITACIONAL, CAJA_AHORRO, TOTAL_DEDUCCION, ACTUALIZACION_ACADEMICA, SUBSIDIO_HIJOS, PRIMA_HOGAR, TOTAL_SUBSIDIO, SUB_TOTAL, SUELDO_FINAL]
		DATA_EXPORT[contador].update(obtenerDiccionarioReport(keySalary, employeeSueldo))
		contador += 1
	exportReport(DATA_EXPORT, NEW_KEYS)
	# print(keySalary)


def executeFile():
	name_file = subprocess.Popen(["explorer.exe", "-p", "/WAIT", "/select"], shell=True)
	print(name_file)
	fileNomina = open('Files/nomina-work.csv', 'r')
	WORD = ""
	DATA = {}
	DATAFINAL = []
	LLAVES = []
	contador = 0
	Nlinea = 0
	for line in fileNomina.readlines():
		for letter in line:
			if(letter == ";" or letter == "\n" ):
				if Nlinea == 0:
					LLAVES.append(WORD) 
				else:	
					key = LLAVES[contador]
					DATA[key] = WORD
					if(contador == len(LLAVES)-1):
						DATAFINAL.append(DATA) 
						DATA = {}
						contador = 0
					else:
						contador += 1
				WORD = "" 
			else:
				WORD += letter
		Nlinea += 1
	generarReportWork(DATAFINAL, LLAVES)
			

if __name__ == '__main__':
	executeFile()





