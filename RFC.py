
nombre = raw_input("Introduce tu nombre: ")
apellido_paterno = raw_input("Introduce tu apellido paterno: ")
apellido_materno = raw_input("Introduce tu apellido materno: ")
dia = raw_input("Introduce tu dia de nacimiento: ")
mes = raw_input("Introduce tu numero de mes de nacimiento: ")
anio = raw_input("Introduce tu anio de nacimiento: ")

nombre = nombre.upper()
apellido_paterno = apellido_paterno.upper()
apellido_materno = apellido_materno.upper()

dia_RFC = "01"
mes_RFC = "01"
anio_RFC = "01"

if not nombre.isalpha() or not apellido_paterno.isalpha() or not apellido_materno.isalpha():
	print "Los datos del nombre no son correctos"
elif not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
	print "Datos de fecha de nacimiento incorrectos"
else:
	if 1 <= int(dia) <= 9:
		 dia_RFC = '0'+ dia
	if 1 <= int(mes) <= 9:
		 mes_RFC = '0'+ mes
	if len(anio) == 4:
		anio_RFC = anio[2:]


Iniciales = apellido_paterno[0:1]+apellido_paterno[2:3]+apellido_materno[:1]+nombre[:1]
Numeros = anio_RFC+mes_RFC+dia_RFC

RFC = Iniciales+Numeros+"XXX"
print RFC