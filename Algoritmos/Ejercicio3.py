# #3.	Un vendedor recibe un sueldo base, más un 10% extra por comisiones 
# de sus ventas. El vendedor desea saber cuánto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realizó en el mes y 
# el total que recibirá tomando en cuenta su sueldo base y sus comisiones.
__BASE_SALARY = 5000000
__PORCENTAGE = 10
__SALES = 3
def bankStatement (salary, porcentage, sales):
	pAmount = (salary * porcentage)/100
	tSales = pAmount * sales
	tFinalSalary = salary + tSales
	print(f"El valor adicional de las ventas es: {tSales}, el Sueldo final es: {tFinalSalary}") 

bankStatement(__BASE_SALARY, __PORCENTAGE, __SALES)
